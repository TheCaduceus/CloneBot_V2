#!/usr/bin/python3
# -*- coding: utf-8 -*-
import html
import logging
import math
import re

from telegram import ParseMode, InlineKeyboardButton
from telegram.utils.helpers import mention_html

from utils.config_loader import config

logger = logging.getLogger(__name__)


def parse_folder_id_from_url(url):
    folder_id = None

    pattern = r'https://drive\.google\.com/(?:' \
              r'drive/(?:u/[\d]+/)?(?:mobile/)?folders/([\w.\-_]+)(?:\?[\=\w]+)?|' \
              r'folderview\?id=([\w.\-_]+)(?:\&[=\w]+)?|' \
              r'open\?id=([\w.\-_]+)(?:\&[=\w]+)?|' \
              r'(?:a/[\w.\-_]+/)?file/d/([\w.\-_]+)|' \
              r'(?:a/[\w.\-_]+/)?uc\?id\=([\w.\-_]+)&?' \
              r')'

    if x := re.search(pattern, url):
        folder_id = ''.join(filter(None, x.groups()))

    if folder_id:
        logger.debug(f'folder_id: {folder_id}')
    return folder_id


def alert_users(context, user_info, warning_message, text):
    mention_html_user = mention_html(user_info.id, html.escape(user_info.full_name))
    message = f'🤔 Detected Suspicious Behaviour from User {mention_html_user} {user_info.id}: {warning_message} {text}.'

    logger.info(message)
    context.bot.send_message(chat_id=config.USER_IDS[0], text=message, parse_mode=ParseMode.HTML)


def get_inline_keyboard_pagination_data(callback_query_prefix, page_data, page_data_chosen=None, page=1,
                                        max_per_page=10):
    callback_query_prefix_data = f'{callback_query_prefix}_page#{page}'
    page_data_len = len(page_data)
    total_page = math.ceil(page_data_len / max_per_page)
    inline_keyboard = []
    for i in range(max((min(page, total_page) - 1) * max_per_page, 0),
                   min(max(page, 1) * max_per_page, page_data_len)):
        if isinstance(page_data[i], list):
            inline_keyboard_row = []
            for j in range(len(page_data[i])):
                is_chosen = any(k == page_data[i][j]['data'] for k in page_data_chosen or [])
                text = f"{'✅ ' if is_chosen else ''}{page_data[i][j]['text']}"
                if page_data[i][j]['data'] != '#':
                    data = f"{f'un{callback_query_prefix_data}' if is_chosen else callback_query_prefix_data},{page_data[i][j]['data']}"

                else:
                    data = '#'
                inline_keyboard_row.append(InlineKeyboardButton(text, callback_data=data))
            inline_keyboard.append(inline_keyboard_row)
        else:
            is_chosen = any(k == page_data[i]['data'] for k in page_data_chosen or [])
            text = f"{'✅ ' if is_chosen else ''}{page_data[i]['text']}"
            if page_data[i]['data'] != '#':
                data = f"{f'un{callback_query_prefix_data}' if is_chosen else callback_query_prefix_data},{page_data[i]['data']}"

            else:
                data = '#'
            inline_keyboard.append(
                [InlineKeyboardButton(text, callback_data=data)])
    if total_page > 1:
        inline_keyboard.extend(get_inline_keyboard_pagination_paginator(callback_query_prefix,
                                                                        total_page,
                                                                        page=page,
                                                                        ))
    return inline_keyboard


def get_inline_keyboard_pagination_paginator(callback_query_prefix, total_page, page=1, total_pages_shown=5):
    start_page = min(max(page - total_pages_shown // 2, 1), max(total_page - total_pages_shown + 1, 1))
    inline_keyboard_pagination_page = [
        InlineKeyboardButton(
            f'{i}' if i != page else f'*{i}',
            callback_data=f'{callback_query_prefix}_page#{i}'
            if i != page
            else '#',
        )
        for i in range(
            start_page, min(start_page + total_pages_shown, total_page + 1)
        )
    ]

    inline_keyboard_pagination = [inline_keyboard_pagination_page]
    if total_page > total_pages_shown:
        previous_1 = max(page - 1, 1)
        previous_2 = max(page - total_pages_shown, 1)
        next_1 = min(page + 1, total_page)
        next_2 = min(page + total_pages_shown, total_page)

        inline_keyboard_pagination_nav = [
            InlineKeyboardButton(
                '|<',
                callback_data=f'{callback_query_prefix}_page#1'
                if page != 1
                else '#',
            ),
            InlineKeyboardButton(
                '<<',
                callback_data=f'{callback_query_prefix}_page#{previous_2}'
                if page != previous_2
                else '#',
            ),
            InlineKeyboardButton(
                '<',
                callback_data=f'{callback_query_prefix}_page#{previous_1}'
                if page != previous_1
                else '#',
            ),
            InlineKeyboardButton(f'{page}/{total_page}', callback_data='#'),
            InlineKeyboardButton(
                '>',
                callback_data=f'{callback_query_prefix}_page#{next_1}'
                if page != next_1
                else '#',
            ),
            InlineKeyboardButton(
                '>>',
                callback_data=f'{callback_query_prefix}_page#{next_2}'
                if page != next_2
                else '#',
            ),
            InlineKeyboardButton(
                '>|',
                callback_data=f'{callback_query_prefix}_page#{total_page}'
                if page != total_page
                else '#',
            ),
        ]

        inline_keyboard_pagination.append(inline_keyboard_pagination_nav)
    return inline_keyboard_pagination


def simplified_path(folder_path):
    max_length = 30

    prefix, delimiter, postfix = folder_path.rpartition('/')
    spare_length = max(max_length - len(postfix), 0)

    # logger.debug(prefix)
    return f"{f'{prefix[:spare_length]}..' if len(prefix) > spare_length else prefix}/{postfix}"
