import os
import requests
import zipfile
import sys
import shutil
from version import __version__

# GitHubのリポジトリ情報
REPO_OWNER = 'aristosptolemy'
REPO_NAME = 'Staff_manegement_project'
BRANCH_NAME = 'main'
CURRENT_VERSION = __version__
VERSION_FILE_URL = f'https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/{BRANCH_NAME}/version.py'
ZIP_URL = f'https://github.com/{REPO_OWNER}/{REPO_NAME}/archive/refs/heads/{BRANCH_NAME}.zip'
GITHUB_API_URL = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/releases/latest'
GITHUB_TOKEN = "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"

class Update_Version:
    def __init__(self):
        pass

    def get_latest_version(self):
        headers = {'Authorization': f'token {GITHUB_TOKEN}'}
        response = requests.get(VERSION_FILE_URL, headers=headers)
        if response.status_code == 200:
            # version.pyファイルの内容を取得
            version_file_content = response.text

            # __version__の値を抽出
            for line in version_file_content.splitlines():
                if line.startswith('__version__'):
                    # バージョン情報を取得
                    latest_version = line.split('=')[1].strip().strip('"\'')
                    return latest_version
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
        latest_version = self.get_latest_version()
        if latest_version and latest_version != CURRENT_VERSION:
            print(f'新しいバージョン {latest_version} が見つかりました。アップデートを開始します。')
            temp_dir = os.path.join(os.getcwd(), 'temp_update')
            os.makedirs(temp_dir, exist_ok=True)
            self.download_and_extract_zip(ZIP_URL, temp_dir)
            self.move_files(os.path.join(temp_dir, f'{REPO_NAME}-{BRANCH_NAME}'), os.getcwd())
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