#!/usr/bin/python3
# -*- coding: utf-8 -*-
import copy
import logging
import os

from googleapiclient import errors
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2 import service_account

from utils.config_loader import config

logger = logging.getLogger(__name__)


class GoogleDrive:
    def __init__(self, user_id):
        service_account_file = os.path.join(config.BASE_PATH,
                                            'gclone_config',
                                            str(user_id),
                                            'current',
                                            'google_drive_puppet.json')

        creds = None
        scopes = ['https://www.googleapis.com/auth/drive']

        if os.path.exists(service_account_file):
            creds = service_account.Credentials.from_service_account_file(
                service_account_file, scopes=scopes)
            if not creds.valid:
                creds.refresh(Request())

        # If there are no (valid) credentials available, throw error.
        if not creds or not creds.valid:
            raise FileNotFoundError

        self.service = build('drive', 'v3', credentials=creds)

    def get_drives(self):
        result = []
        page_token = None
        while True:
            try:
                param = {
                    'pageSize': 100,
                }
                if page_token:
                    param['pageToken'] = page_token
                drives = self.service.drives().list(**param).execute()

                result.extend(drives['drives'])
                logger.debug(f"Received {len(drives['drives'])} drives")
                page_token = drives.get('nextPageToken')
                if not page_token:
                    break
            except errors.HttpError as error:
                logger.warning(f'An error occurred: {error}')
                break
        return {item['id']: item['name'] for item in result}

    def get_file_name(self, file_id):
        param = {
            'fileId': file_id,
            'supportsAllDrives': True,
            'fields': 'name, driveId',
        }
        file_info = self.service.files().get(**param).execute()
        file_name = file_info['name']
        if file_info.get('driveId', None) == file_id:
            file_name = self.get_drive_name(file_id)
        return file_name

    def get_file_path_from_id(self, file_id, parents=[]):
        result = copy.deepcopy(parents)
        param = {
            'fileId': file_id,
            'supportsAllDrives': True,
            'fields': 'name, mimeType, parents, driveId',
        }
        file_info = self.service.files().get(**param).execute()
        if file_info.get('driveId', None) == file_id:
            drive_name = self.get_drive_name(file_id)
            parent_entry = {'name': drive_name, 'folder_id': file_id}
        else:
            parent_entry = {'name': file_info['name'], 'folder_id': file_id}
        parent = file_info.get('parents', None)
        result.append(parent_entry)
        if parent:
            return self.get_file_path_from_id(parent[0], result)
        logger.debug(str(result))
        return result

    def get_drive_name(self, drive_id):
        param = {
            'driveId': drive_id,
        }
        drive_info = self.service.drives().get(**param).execute()
        return drive_info['name']

    def list_folders(self, folder_id):
        result = []

        page_token = None
        while True:
            try:
                param = {
                    'q': f"'{folder_id}' in parents and mimeType = 'application/vnd.google-apps.folder' and trashed = false",
                    'includeItemsFromAllDrives': True,
                    'supportsAllDrives': True,
                    'fields': 'nextPageToken, files(id, name)',
                    'pageSize': 1000,
                }

                if page_token:
                    param['pageToken'] = page_token
                all_files = self.service.files().list(**param).execute()

                result.extend(all_files['files'])
                logger.debug(f"Received {len(all_files['files'])} files")
                page_token = all_files.get('nextPageToken')

                if not page_token:
                    break
            except errors.HttpError as error:
                logger.info(f'An error occurred: {error}')
                break
        result_sorted = sorted(result, key=lambda k: k['name'])
        return {item['id']: item['name'] for item in result_sorted}

    def get_folder_link(self, folder_id, folder_path):
        folder_path_list = list(filter(None, folder_path.split('/')))
        if result := self.get_folder_id_by_name(folder_id, folder_path_list[0]):
            if len(folder_path_list) > 1:
                for item in result:
                    next_result = self.get_folder_link(item['id'], '/'.join(folder_path_list[1:]))
                    if isinstance(next_result, str):
                        return next_result
                return None
            else:
                link = f"https://drive.google.com/open?id={result[0]['id']}"
                logger.info(f'found link: {link}')
                return link
        return None

    def get_folder_id_by_name(self, folder_id, folder_name):
        page_token = None
        result = []
        while True:
            try:
                param = {
                    'q': f"name = '{folder_name}' and mimeType = 'application/vnd.google-apps.folder' and '{folder_id}' in parents and trashed = false",
                    'includeItemsFromAllDrives': True,
                    'supportsAllDrives': True,
                    'fields': 'nextPageToken, files(id, name)',
                    'pageSize': 1000,
                }

                if page_token:
                    param['pageToken'] = page_token
                # logger.debug(str(param))
                all_files = self.service.files().list(**param).execute()

                result.extend(all_files['files'])
                # logger.debug(str(allFiles))
                # logger.info('Received {} files'.format(len(allFiles['files'])))
                page_token = all_files.get('nextPageToken')

                if not page_token:
                    break
            except errors.HttpError as error:
                logger.info(f'An error occurred: {error}')
                break
        return result
