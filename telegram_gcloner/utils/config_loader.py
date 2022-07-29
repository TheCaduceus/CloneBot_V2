#!/usr/bin/python3
# -*- coding: utf-8 -*-

import configparser
import logging
import os
import shutil
import sys


logger = logging.getLogger(__name__)


class _Config:
    def __init__(self):
        self._ad_string = ''
        self._log_file = ''
        self._telegram_token = None
        self._path_to_gclone = None
        self._user_ids = ''
        self._group_ids = ''
        self._gclone_para_override = ''
        self._base_path = os.path.dirname(os.path.dirname(__file__))
        self.TIMER_TO_DELETE_MESSAGE = 20
        self.AD_STRING = ' Goodbye, Please talk to the Bot<a href="{}"> privately.</a>'

    def load_config(self):
        logger.debug('Loading config')

        try:
            config_file = configparser.ConfigParser(allow_no_value=True)
            config_file.read(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.ini'), encoding='utf-8')
        except IOError as err:
            logger.warning("Can't open the config file: ", err)
            input('Press enter to exit.')
            sys.exit(1)

        if not config_file.has_section('General'):
            logger.warning("Can't find General section in the Config File.")
            input('Press enter to exit.')
            sys.exit(1)

        config_general = config_file['General']

        config_general_keywords_str = [
            'telegram_token',
            'user_ids',
            'group_ids',
        ]

        self.get_config_from_section('str', config_general_keywords_str, config_general)
        self.get_config_from_section('str', ['path_to_gclone', 'gclone_para_override'], config_general, optional=True)

        self._user_ids = [int(item) for item in self._user_ids.split(',')]
        self._group_ids = [int(item) for item in self._group_ids.split(',')]

        if not os.path.isfile(self._path_to_gclone):
            self._path_to_gclone = shutil.which('gclone')
            if not self._path_to_gclone:
                logger.warning('Gclone Executable was not found in the Drectory.')
                input("Press Enter to continue...")
                sys.exit(0)
        logger.info(f'Found gclone: {self._path_to_gclone}')

        if not self._telegram_token:
            logger.warning('Telegram Bot Token not found.')
            input("Press Enter to continue...")
            sys.exit(0)
        logger.info(f'Found Bot Token: {self._telegram_token}')

        if self._gclone_para_override:
            self._gclone_para_override = self._gclone_para_override.split()

    def get_config_from_section(self, var_type, keywords, section, optional=False):
        for item in keywords:
            if var_type == 'int':
                value = section.getint(item, 0)
            elif var_type == 'str':
                value = section.get(item, '')
            elif var_type == 'bool':
                value = section.getboolean(item, False)
            else:
                raise TypeError
            if not optional and not value and value is not False:
                logger.warning(f'{item} is not provided.')
                input("Press Enter to continue...")
                sys.exit(1)
            logger.info(f'Found {item}: {value}')
            setattr(self, f'_{item}', value)

    @property
    def PATH_TO_GCLONE(self):
        return self._path_to_gclone

    @property
    def TELEGRAM_TOKEN(self):
        return self._telegram_token

    @property
    def USER_IDS(self):
        return self._user_ids

    @property
    def GROUP_IDS(self):
        return self._group_ids

    @property
    def GCLONE_PARA_OVERRIDE(self):
        return self._gclone_para_override

    @property
    def BASE_PATH(self):
        return self._base_path

    @property
    def LOG_FILE(self):
        return self._log_file

    @LOG_FILE.setter
    def LOG_FILE(self, val):
        self._log_file = val


config = _Config()