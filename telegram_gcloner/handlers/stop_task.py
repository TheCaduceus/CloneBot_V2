#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging
import re

from telegram.ext import Dispatcher, CallbackQueryHandler

from utils.fire_save_files import thread_pool
from utils.helper import alert_users
from utils.restricted import restricted

logger = logging.getLogger(__name__)

regex_stop_task = r'^stop_task,(\d+)'


def init(dispatcher: Dispatcher):
    """Provide handlers initialization."""
    dispatcher.add_handler(CallbackQueryHandler(stop_task, pattern=regex_stop_task))


@restricted
def stop_task(update, context):
    query = update.callback_query
    if query.message.chat_id < 0 and \
            (not query.message.reply_to_message or
             query.from_user.id != query.message.reply_to_message.from_user.id):
        alert_users(context, update.effective_user, 'invalid caller', query.data)
        query.answer(text='Yo-he!', show_alert=True)
        return
    if query.data:
        if match := re.search(regex_stop_task, query.data):
            thread_id = int(match[1])
            if tasks := thread_pool.get(update.effective_user.id, None):
                for t in tasks:
                    if t.ident == thread_id and t.owner == query.from_user.id:
                        t.kill()
                        logger.info(f'User {query.from_user.id} has stopped Cloning Task {thread_id}')
                        return
    alert_users(context, update.effective_user, 'invalid query data', query.data)
    query.answer(text='Yo-he!', show_alert=True)
    return
