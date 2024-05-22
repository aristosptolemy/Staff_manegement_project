import os
import requests
import zipfile
from version import __version__


# GitHubのリポジトリ情報
REPO_OWNER = 'username'
REPO_NAME = 'repository'
CURRENT_VERSION = '1.0.0'
VERSION_FILE_URL = f'https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/main/version.txt'
ZIP_URL = f'https://github.com/{REPO_OWNER}/{REPO_NAME}/archive/refs/heads/main.zip'

class Update_version:
    def __init__(self):
        self.check_for_updates()
        
        
    def get_latest_version(self):
        response = requests.get(VERSION_FILE_URL)
        if response.status_code == 200:
            return response.text.strip()
        return None

    def download_and_extract_zip(self,url, extract_to='.'):
        response = requests.get(url)
        zip_path = os.path.join(extract_to, 'update.zip')
        with open(zip_path, 'wb') as f:
            f.write(response.content)
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        os.remove(zip_path)

    def check_for_updates(self):
        latest_version = self.get_latest_version()
        if latest_version and latest_version != CURRENT_VERSION:
            print(f'新しいバージョン {latest_version} が見つかりました。アップデートを開始します。')
            self.download_and_extract_zip(ZIP_URL)
            print('アップデートが完了しました。')
        else:
            print('最新バージョンです。')
