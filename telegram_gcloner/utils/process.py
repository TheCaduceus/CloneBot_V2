#!/usr/bin/python3
# -*- coding: utf-8 -*-
import html
import logging


from telegram import ParseMode
from telegram.utils.helpers import mention_html

from utils.config_loader import config

logger = logging.getLogger(__name__)


def leave_chat_from_message(message, context):
    context.bot.send_message(
        chat_id=message.chat_id,
        text=f'Hey, Thank you for adding CloneBot V2 to this group. {config.AS_STRING.format(context.bot.username)}',
        parse_mode=ParseMode.HTML,
    )

    context.bot.send_message(chat_id=message.chat_id, text='\n\nUnfortunately I am not authorized in this Group/Chat 😔 \n So I am leavng this Group \nIf you want me in this Group/Chat, ask my owner to authorize me here 😉.')
    if message.from_user:
        mention_html_from_user = mention_html(message.from_user.id,
                                              message.from_user.full_name.full_name)
        text = f'🔙 Left Unauthorized Group : \n │ Name : {html.escape(message.chat.title)} ({message.chat_id}). \n │ Added by : {mention_html_from_user} {message.from_user.id}. \n │ Message : {message.text}'

    else:
        text = f'🔙 Left Unauthorized Group : \n │ Name : {html.escape(message.chat.title)} ({message.chat_id}). \n │ Message : {message.text}'

    context.bot.leave_chat(message.chat_id)
    logger.warning(text)
    context.bot.send_message(chat_id=config.USER_IDS[0], text=text, parse_mode=ParseMode.HTML)
