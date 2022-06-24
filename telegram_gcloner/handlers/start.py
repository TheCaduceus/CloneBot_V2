#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging

from telegram.ext import Dispatcher, CommandHandler

from utils.callback import callback_delete_message
from utils.config_loader import config
from utils.restricted import restricted

logger = logging.getLogger(__name__)


def init(dispatcher: Dispatcher):
    """Provide handlers initialization."""
    dispatcher.add_handler(CommandHandler('start', start))


@restricted
def start(update, context):
    rsp = update.message.reply_text('🔺 First, send me a ZIP archive containing the SA files and add /sa to the subject. 🔺\n'
                                    '📂 After that, use /folders to set and mark/favourite your destination folders. 📂\n'
                                    '🔗 You are now ready to go! Just forward or send a Google Drive link to clone the File/Folder 🔗 \n.'
                                    'Bot Developed by Dr.Caduceus & MsGsuite . Follow @TheCaduceus & @MsGsuite on Telegram')
    rsp.done.wait(timeout=60)
    message_id = rsp.result().message_id
    if update.message.chat_id < 0:
        context.job_queue.run_once(callback_delete_message, config.TIMER_TO_DELETE_MESSAGE,
                                   context=(update.message.chat_id, message_id))
        context.job_queue.run_once(callback_delete_message, config.TIMER_TO_DELETE_MESSAGE,
                                   context=(update.message.chat_id, update.message.message_id))
