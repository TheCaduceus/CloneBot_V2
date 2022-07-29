#!/usr/bin/python3
# -*- coding: utf-8 -*-
import copy
import logging

from telegram import Update
from telegram.ext import Dispatcher, CommandHandler, CallbackContext, Filters

from utils.config_loader import config
from utils.restricted import restricted_admin

logger = logging.getLogger(__name__)


def init(dispatcher: Dispatcher):
    """Provide handlers initialization."""
    dispatcher.add_handler(CommandHandler('vip', vip, filters=Filters.chat(config.USER_IDS[0]), pass_args=True))
    dispatcher.add_handler(CommandHandler('unvip', unvip, filters=Filters.chat(config.USER_IDS[0]), pass_args=True))


@restricted_admin
def vip(update: Update, context: CallbackContext):
    if not context.args:
        if vip_list := context.bot_data.get('vip', None):
            update.message.reply_text('\n'.join(map(str, vip_list)))
        return
    if not context.args[0].isdigit:
        update.message.reply_text('/vip user_id')
        return
    user_id = int(context.args[0])
    if not context.bot_data.get('vip', None):
        context.bot_data['vip'] = [user_id]
    elif user_id not in context.bot_data['vip']:
        new_vip = copy.deepcopy(context.bot_data['vip'])
        new_vip.append(user_id)
        context.bot_data['vip'] = new_vip
    else:
        update.message.reply_text('User already Exists in VIP Users List.')
        return
    context.dispatcher.update_persistence()
    update.message.reply_text('User added successfully to VIP Users List.')
    logger.info(f'{user_id} is added successfully to VIP Users List.')
    return


@restricted_admin
def unvip(update: Update, context: CallbackContext):
    if not context.args or not context.args[0].isdigit:
        update.message.reply_text('/unvip user_id')
        return
    user_id = int(context.args[0])
    if user_id in context.bot_data.get('vip', []):
        new_vip = copy.deepcopy(context.bot_data['vip'])
        new_vip.remove(user_id)
        context.bot_data['vip'] = new_vip
        context.dispatcher.update_persistence()
        update.message.reply_text('Removed from VIP.')
        logger.info(f'{user_id} is successfully removed from VIP Users List.')
    else:
        update.message.reply_text('Could not find User in VIP Users List.')

    return
