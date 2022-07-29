#!/usr/bin/python3
# -*- coding: utf-8 -*-
import html
import logging
import re

from telegram import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Dispatcher, CallbackQueryHandler

from utils.fire_save_files import MySaveFileThread, thread_pool
from utils.google_drive import GoogleDrive
from utils.helper import parse_folder_id_from_url, alert_users, get_inline_keyboard_pagination_data, simplified_path

logger = logging.getLogger(__name__)

udkey_folders = 'folder_ids'


def init(dispatcher: Dispatcher):
    """Provide handlers initialization."""
    dispatcher.add_handler(CallbackQueryHandler(save_to_folder_page,
                                                pattern=r'^save_to_folder_page#\d+$'))
    dispatcher.add_handler(CallbackQueryHandler(save_to_folder,
                                                pattern=r'^save_to_folder(:?_page#\d+)?\,\s*[\dA-Za-z\-_]+$'))


def parse_entity_for_drive_id(message):
    if message.photo:
        entities = message.parse_caption_entities()
    else:
        entities = message.parse_entities()

    folder_ids = {}
    k = 0

    for entity in entities:
        if entity.type == 'text_link':
            url = entity.url
            name = entities[entity]
        elif entity.type == 'url':
            url = entities[entity]
            name = 'file{:03d}'.format(k)
        else:
            continue

        logger.debug('Found {0}: {1}.'.format(name, url))
        folder_id = parse_folder_id_from_url(url)
        if not folder_id:
            continue
        folder_ids[folder_id] = name

        logger.debug('Found {0} with folder_id {1}.'.format(name, folder_id))

    if not folder_ids:
        logger.debug('Cannot find any legit folder id.')
        return None
    return folder_ids


def process_drive_links(update, context):
    if not update.message:
        return

    folder_ids = parse_entity_for_drive_id(update.message)

    if not folder_ids:
        return
    message = '📑 The Following Files were Detected : 📑\n'

    try:
        gd = GoogleDrive(update.effective_user.id)
    except Exception as e:
        update.message.reply_text(
            f'🔸 Please make sure the SA archive has been uploaded and the collection folder has been configured. 🔸\n{e}'
        )

        return

    for item in folder_ids:
        try:
            folder_name = gd.get_file_name(item)
        except Exception as e:
            update.message.reply_text(
                f'🔸 Please make sure that the SA archive has been uplaoded and yuor SA have rights to read files from the Source Link. 🔸\n{e}'
            )

            return
        message += f'     <a href="https://drive.google.com/open?id={item}">{html.escape(folder_name)}</a>\n'

    message += '\n📂 Please select the Target Destination 📂'
    if fav_folder_ids := context.user_data.get(udkey_folders, None):
        page_data = [
            {
                'text': simplified_path(fav_folder_ids[item]['path']),
                'data': f'{item}',
            }
            for item in fav_folder_ids
        ]

        callback_query_prefix = 'save_to_folder'
        page = 1
        inline_keyboard_drive_ids = get_inline_keyboard_pagination_data(
            callback_query_prefix,
            page_data,
            page=page,
            max_per_page=10,
        )
    else:
        inline_keyboard_drive_ids = [[InlineKeyboardButton(text='⚠️ Use /folders to add a destination to Favourite Folders List ⚠️', callback_data='#')]]
    inline_keyboard = inline_keyboard_drive_ids
    update.message.reply_text(message, parse_mode=ParseMode.HTML,
                              disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(inline_keyboard))


def save_to_folder_page(update, context):
    query = update.callback_query
    if query.message.chat_id < 0 and \
            (not query.message.reply_to_message or
             query.from_user.id != query.message.reply_to_message.from_user.id):
        alert_users(context, update.effective_user, 'invalid caller', query.data)
        query.answer(text='Yo-he!', show_alert=True)
        return
    match = re.search(r'^save_to_folder_page#(\d+)$', query.data)
    if not match:
        alert_users(context, update.effective_user, 'invalid query data', query.data)
        query.answer(text='Yo-he!', show_alert=True)
        return
    page = int(match[1])
    if fav_folder_ids := context.user_data.get(udkey_folders, None):
        page_data = [
            {
                'text': simplified_path(fav_folder_ids[item]['path']),
                'data': f'{item}',
            }
            for item in fav_folder_ids
        ]

        callback_query_prefix = 'save_to_folder'

        inline_keyboard_drive_ids = get_inline_keyboard_pagination_data(
            callback_query_prefix,
            page_data,
            page=page,
            max_per_page=10,
        )
    else:
        inline_keyboard_drive_ids = [[InlineKeyboardButton(text='🔹 If you don\'t have any shared drives, you must get one here : @MsGsuite before you can use this.', callback_data='#')]]
    inline_keyboard = inline_keyboard_drive_ids
    query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(inline_keyboard))


def save_to_folder(update, context):
    query = update.callback_query
    if query.message.chat_id < 0 and \
            (not query.message.reply_to_message or
             query.from_user.id != query.message.reply_to_message.from_user.id):
        alert_users(context, update.effective_user, 'invalid caller', query.data)
        query.answer(text='Yo-he!', show_alert=True)
        return
    match = re.search(r'^save_to_folder(?:_page#[\d]+)?,\s*([\dA-Za-z\-_]+)$', query.data)
    fav_folders = context.user_data.get(udkey_folders, {})
    if not match or match[1] not in fav_folders:
        alert_users(context, update.effective_user, 'invalid query', query.data)
        query.answer(text='Yo-he!', show_alert=True)
        return
    message = query.message
    text = message.caption or message.text
    folder_ids = parse_entity_for_drive_id(message)

    if not folder_ids:
        return
    dest_folder = fav_folders[match[1]]
    dest_folder['folder_id'] = match[1]
    if not thread_pool.get(update.effective_user.id, None):
        thread_pool[update.effective_user.id] = []
    t = MySaveFileThread(args=(update, context, folder_ids, text, dest_folder))
    thread_pool[update.effective_user.id].append(t)
    t.start()
    logger.debug(f'User {query.from_user.id} has added task {t.ident}.')
    query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(
        [[InlineKeyboardButton(text='Executed', callback_data='#')]]))
