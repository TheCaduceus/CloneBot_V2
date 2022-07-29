#!/usr/bin/python3
# -*- coding: utf-8 -*-
import copy
import html
import logging
import re

from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from telegram.ext import Dispatcher, CommandHandler, CallbackQueryHandler

from utils.config_loader import config
from utils.google_drive import GoogleDrive
from utils.helper import alert_users, get_inline_keyboard_pagination_data, simplified_path
from utils.restricted import restricted

logger = logging.getLogger(__name__)

default_max_folders = 4
default_max_folders_vip = 10

udkey_folders = 'folder_ids'
udkey_folders_cache = 'folder_ids_cache'
udkey_fav_folders_replace = 'favourite_folder_ids_replace'


def init(dispatcher: Dispatcher):
    """Provide handlers initialization."""
    dispatcher.add_handler(
        CallbackQueryHandler(choose_folder,
                             pattern=r'^(?:un)?choose_folder(?:_replace)?(?:_page#\d+)?(?:\,[\dA-Za-z\-_]+)?$'))
    dispatcher.add_handler(CallbackQueryHandler(chosen_folder,
                                                pattern=r'^chosen_folder\,[\dA-Za-z\-_]+$'))
    dispatcher.add_handler(CommandHandler('folders', set_folders))
    dispatcher.add_handler(CallbackQueryHandler(set_folders,
                                                pattern=r'^(?:un)?set_folders(:?_page#\d+)?(?:\,[\dA-Za-z\-_]+)?$'))


@restricted
def chosen_folder(update, context):
    query = update.callback_query
    if query.message.chat_id < 0 and \
            (not query.message.reply_to_message or
             query.from_user.id != query.message.reply_to_message.from_user.id):
        alert_users(context, update.effective_user, 'invalid caller', query.data)
        query.answer(text='Yo-he!', show_alert=True)
        return
    if update.effective_user.id in config.USER_IDS\
            or (context.bot_data.get('vip', None) and update.effective_user.id in context.bot_data['vip']):
        max_folders = default_max_folders_vip
    else:
        max_folders = default_max_folders

    callback_query_prefix = 'chosen_folder'

    try:
        gd = GoogleDrive(update.effective_user.id)
    except Exception as e:
        context.bot.send_message(
            chat_id=update.effective_user.id,
            text=f'🔸 Please make sure the SA archive has been uploaded followed by /sa and the Destination Favourite Folder has been configured. 🔸\n<code>{html.escape(str(e))}</code>',
            parse_mode=ParseMode.HTML,
        )

        return

    query = update.callback_query
    match = re.search(
        f'^{callback_query_prefix},(?P<folder_id>[\dA-Za-z\-_]+)$', query.data
    )

    if not match:
        alert_users(context, update.effective_user, 'invalid query', query.data)
        query.answer(text='Yo-he!', show_alert=True)
        return
    folder_id = match['folder_id']

    drive_ids_replace = context.user_data.get(udkey_fav_folders_replace, None)
    favourite_drive_ids = context.user_data.get(udkey_folders, {})
    new_fav_folders = copy.deepcopy(favourite_drive_ids)
    new_fav_folders.pop(drive_ids_replace, None)
    new_fav_folders_len = len(new_fav_folders)
    if new_fav_folders_len < max_folders:
        current_path_list = gd.get_file_path_from_id(folder_id)
        if not current_path_list:
            alert_users(context, update.effective_user, 'invalid folder id', query.data)
            query.answer(text='Yo-he!', show_alert=True)
            return
        current_path_list.reverse()
        new_fav_folders[folder_id] = {
            'name': current_path_list[-1]['name'],
            'path': '/' + '/'.join(item['name'] for item in current_path_list),
        }
        context.user_data[udkey_folders] = new_fav_folders
        context.user_data[udkey_fav_folders_replace] = None
        context.dispatcher.update_persistence()
        set_folders(update, context)
    else:
        query.answer(text=f'Maximum {max_folders}', show_alert=True)
    return


@restricted
def choose_folder(update, context):
    current_folder_id = ''
    folders = None

    try:
        gd = GoogleDrive(update.effective_user.id)
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_user.id,
                                 text='🔸 Please make sure the SA archive has been uploaded followed by /sa and the Destination Favourite Folder has been configured. 🔸\n'
                                      '<code>{}</code>'.format(html.escape(str(e))),
                                 parse_mode=ParseMode.HTML)
        return

    if context.args:
        current_folder_id = context.args[0]
        try:
            gd.get_file_name(current_folder_id)
            folders = gd.list_folders(current_folder_id)
        except Exception as e:
            folders = gd.get_drives()
            current_folder_id = ''
            context.bot.send_message(chat_id=update.effective_user.id,
                                     text='Error：\n<code>{}</code>'.format(html.escape(str(e))),
                                     parse_mode=ParseMode.HTML)

    callback_query_prefix = 'choose_folder'
    query = update.callback_query
    page = None
    message_id = -1
    if not query:
        rsp = update.message.reply_text('⚙️ Getting Directory ⚙️')
        rsp.done.wait(timeout=60)
        message_id = rsp.result().message_id
        if not folders:
            folders = gd.get_drives()
            context.user_data[udkey_folders_cache] = copy.deepcopy(folders)

    if query:
        logger.debug('{}: {}'.format(update.effective_user.id, query.data))
        if query.message.chat_id < 0 and \
                (not query.message.reply_to_message or
                 query.from_user.id != query.message.reply_to_message.from_user.id):
            alert_users(context, update.effective_user, 'invalid caller', query.data)
            query.answer(text='Yo-he!', show_alert=True)
            return
        message_id = query.message.message_id
        match = re.search(r'^(?P<un>un)?{}(?P<replace>_replace)?(?:_page#(?P<page>\d+))?'
                          r'(?:,(?P<folder_id>[\dA-Za-z\-_]+))?$'.format(callback_query_prefix),
                          query.data)
        if match:
            match_folder_id = match.group('folder_id')
            if match_folder_id:
                current_folder_id = match_folder_id
                try:
                    gd.get_file_name(current_folder_id)
                    folders = gd.list_folders(match_folder_id)
                except Exception as e:
                    folders = gd.get_drives()
                    current_folder_id = ''
                    context.bot.send_message(chat_id=update.effective_user.id,
                                             text='⁉️ Error：\n<code>{}</code>'.format(html.escape(str(e))),
                                             parse_mode=ParseMode.HTML)
                context.user_data[udkey_folders_cache] = copy.deepcopy(folders)
                if not folders:
                    folders = {'#': '(No subfolders)'}
                match_folder_id_replace = match.group('replace')
                if match_folder_id_replace:
                    context.user_data[udkey_fav_folders_replace] = match_folder_id
            if match.group('page'):
                page = int(match.group('page'))
            if not folders and match.group('page'):
                folders = context.user_data.get(udkey_folders_cache, None)
            if not folders:
                folders = gd.get_drives()
                context.user_data[udkey_folders_cache] = copy.deepcopy(folders)
            if not folders:
                folders = {'#': 'I could not find any Shared Drives associated with your Service Accounts. \n If you don`t have no shared drives, go to @MsGsuite to get one for yourself.'}
        else:
            alert_users(context, update.effective_user, 'invalid query data', query.data)
            query.answer(text='Yo-he!', show_alert=True)
            return

    if not page:
        page = 1

    folders_len = len(folders)
    page_data = []
    for item in folders:
        page_data.append({'text': folders[item], 'data': item})

    page_data_chosen = list(context.user_data.get(udkey_folders, {}))
    inline_keyboard_drive_ids = get_inline_keyboard_pagination_data(
        callback_query_prefix,
        page_data,
        page_data_chosen=page_data_chosen,
        page=page,
        max_per_page=10,
    )

    if current_folder_id:
        current_path = ''
        current_path_list = gd.get_file_path_from_id(current_folder_id)
        if current_path_list:
            current_folder_name = current_path_list[0]['name']
            for item in current_path_list:
                current_path = '/{}{}'.format(item['name'], current_path)
            if len(current_path_list) > 1:
                inline_keyboard_drive_ids.insert(
                    0, [InlineKeyboardButton('📁 ' + current_path,
                                             callback_data='{},{}'.format(
                                                 callback_query_prefix, current_path_list[1]['folder_id']))])
            else:
                inline_keyboard_drive_ids.insert(
                    0, [InlineKeyboardButton('📁' + current_path,
                                             callback_data=callback_query_prefix)])
            inline_keyboard_drive_ids.append(
                [InlineKeyboardButton('✔️ Select this folder({})'.format(current_folder_name),
                                      callback_data='chosen_folder,{}'.format(current_folder_id))])
    inline_keyboard_drive_ids.append([InlineKeyboardButton('🔙 Go back',
                                                           callback_data='choose_folder' if current_folder_id else '#'),
                                      InlineKeyboardButton('Cancel', callback_data='cancel')])
    context.bot.edit_message_text(chat_id=update.effective_chat.id,
                                  message_id=message_id,
                                  text='🔶 Select the directory you wish to add to Favourite Folders and also want to use for cloning 🔶 \n 🔶🔶 There are {} subdirectories found 🔶🔶'.format(
                                      folders_len),
                                  reply_markup=InlineKeyboardMarkup(inline_keyboard_drive_ids))


@restricted
def set_folders(update, context):
    if update.effective_user.id in config.USER_IDS\
            or (context.bot_data.get('vip', None) and update.effective_user.id in context.bot_data['vip']):
        max_folders = default_max_folders_vip
    else:
        max_folders = default_max_folders

    callback_query_prefix = 'choose_folder'
    query = update.callback_query
    page = 1
    if not query:
        rsp = update.message.reply_text('⚙️ Getting Favourite Shared Drives ⚙️')
        rsp.done.wait(timeout=60)
        message_id = rsp.result().message_id
    else:
        if query.message.chat_id < 0 and \
                (not query.message.reply_to_message or
                 query.from_user.id != query.message.reply_to_message.from_user.id):
            alert_users(context, update.effective_user, 'invalid caller', query.data)
            query.answer(text='Yo-he!', show_alert=True)
            return
        message_id = query.message.message_id
    folder_ids = context.user_data.get(udkey_folders, None)

    if folder_ids:
        folder_ids_len = len(folder_ids)
        page_data = []
        for item in folder_ids:
            page_data.append({'text': simplified_path(folder_ids[item]['path']), 'data': '{}'.format(item)})
        inline_keyboard_drive_ids = get_inline_keyboard_pagination_data(
            callback_query_prefix + '_replace',
            page_data,
            page=page,
            max_per_page=10,
        )
    else:
        inline_keyboard_drive_ids = []
        folder_ids_len = 0
    if folder_ids_len < max_folders:
        inline_keyboard_drive_ids.insert(0, [InlineKeyboardButton('➕ Add Favorite Folder', callback_data=callback_query_prefix)])
    inline_keyboard_drive_ids.append([InlineKeyboardButton('✔️ Done', callback_data='cancel')])

    context.bot.edit_message_text(chat_id=update.effective_chat.id,
                                  message_id=message_id,
                                  text='📁 Total No of Destination Folders {}/{} 📁：'.format(
                                      folder_ids_len,
                                      max_folders,
                                  ),
                                  reply_markup=InlineKeyboardMarkup(inline_keyboard_drive_ids))
