#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging

from telegram.ext import Dispatcher, MessageHandler, Filters, CallbackQueryHandler

from handlers.process_drive_links import process_drive_links
from utils.config_loader import config
from utils.helper import parse_folder_id_from_url, alert_users
from utils.process import leave_chat_from_message
from utils.restricted import restricted_admin, restricted

logger = logging.getLogger(__name__)


def init(dispatcher: Dispatcher):
    """Provide handlers initialization."""
    dispatcher.add_handler(
        MessageHandler(Filters.chat_type.groups & Filters.chat(config.GROUP_IDS) &
                       (Filters.text | Filters.caption) &
                       ~Filters.update.edited_message,
                       process_message))
    dispatcher.add_handler(
        MessageHandler(Filters.chat(config.USER_IDS[0]) &
                       (Filters.text | Filters.caption) &
                       ~Filters.update.edited_message,
                       process_message_from_authorised_user))
    dispatcher.add_handler(
        MessageHandler((~Filters.chat_type.groups) &
                       (Filters.text | Filters.caption) &
                       ~Filters.update.edited_message,
                       process_message))

    dispatcher.add_handler(CallbackQueryHandler(ignore_callback, pattern=r'^#$'))
    dispatcher.add_handler(CallbackQueryHandler(get_warning))


def ignore_callback(update, context):
    query = update.callback_query
    query.answer(text='')


def get_warning(update, context):
    query = update.callback_query
    alert_users(context, update.effective_user, 'unknown query data', query.data)
    query.answer(text='Yo-he!', show_alert=True)


def leave_from_chat(update, context):
    if update.channel_post:
        if update.channel_post.chat_id < 0 and update.channel_post.chat_id not in config.GROUP_IDS:
            leave_chat_from_message(update.channel_post, context)
        return
    elif update.message.chat_id < 0 and update.message.chat_id not in config.GROUP_IDS:
        leave_chat_from_message(update.message, context)
        return


@restricted_admin
def process_message_from_authorised_user(update, context):
    logger.debug(update.message)
    if update.message.caption:
        text_urled = update.message.caption_html_urled
    else:
        text_urled = update.message.text_html_urled
    if parse_folder_id_from_url(text_urled):
        process_drive_links(update, context)
        return


@restricted
def process_message(update, context):
    if not update.message:
        return
    if update.message.chat_id != config.USER_IDS[0]:
        logger.debug(update.message)
        if update.message.caption:
            text_urled = update.message.caption_html_urled
        else:
            text_urled = update.message.text_html_urled
        if parse_folder_id_from_url(text_urled):
            process_drive_links(update, context)
            return
