import os
import requests
import zipfile
import sys
import shutil
from version import __version__


# GitHubのリポジトリ情報
REPO_OWNER = 'aristosptolemy'
REPO_NAME = 'Staff_manegement_project'
CURRENT_VERSION = __version__
VERSION_FILE_URL = f'https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/main/version.txt'
ZIP_URL = f'https://github.com/{REPO_OWNER}/{REPO_NAME}/archive/refs/heads/main.zip'
GITHUB_API_URL = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/releases/latest'
GITHUB_TOKEN = "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"


class UpdateVersion:
    def __init__(self):
        pass

    def get_latest_version_info(self):
        headers = {'Authorization': f'token {GITHUB_TOKEN}'}
        response = requests.get(GITHUB_API_URL, headers=headers)
        if response.status_code == 200:
            return response.json()
        return None

    def download_and_extract_zip(self, url, extract_to='.'):
        headers = {'Authorization': f'token {GITHUB_TOKEN}'}
        response = requests.get(url, headers=headers)
        zip_path = os.path.join(extract_to, 'update.zip')
        with open(zip_path, 'wb') as f:
            f.write(response.content)
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        os.remove(zip_path)

    def move_files(self, src, dst):
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                if os.path.exists(d):
                    shutil.rmtree(d)
                shutil.move(s, d)
            else:
                if os.path.exists(d):
                    os.remove(d)
                shutil.move(s, d)

    def check_for_updates(self):
        latest_release = self.get_latest_version_info()
        if latest_release:
            latest_version = latest_release['tag_name']
            if latest_version != CURRENT_VERSION:
                print(f'新しいバージョン {latest_version} が見つかりました。アップデートを開始します。')
                asset = next(item for item in latest_release['assets'] if item['name'].endswith('.zip'))
                temp_dir = os.path.join(os.getcwd(), 'temp_update')
                os.makedirs(temp_dir, exist_ok=True)
                self.download_and_extract_zip(asset['browser_download_url'], temp_dir)
                self.move_files(os.path.join(temp_dir, f'{REPO_NAME}-{latest_version}'), os.getcwd())
                shutil.rmtree(temp_dir)
                print('アップデートが完了しました。再起動します。')
                self.restart_application()
                return True
        else:
            print('最新バージョンです。')
            return False

    def restart_application(self):
        # 現在のスクリプトを再起動
        python = sys.executable
        os.execl(python, python, *sys.argv)