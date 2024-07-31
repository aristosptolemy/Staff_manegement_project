import os
import requests
import zipfile
import sys
import shutil
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from data.version import __version__


# GitHubのリポジトリ情報
REPO_OWNER = 'aristosptolemy'
REPO_NAME = 'Staff_manegement_project'
BRANCH_NAME = 'main'
CURRENT_VERSION = __version__
print(CURRENT_VERSION)
#https://github.com/aristosptolemy/Staff_manegement_project/blob/main/staff_manegement_app/data/version.py
VERSION_FILE_URL = 'https://raw.githubusercontent.com/aristosptolemy/Staff_manegement_project/main/staff_manegement_app/data/version.py'
ZIP_URL = f'https://github.com/{REPO_OWNER}/{REPO_NAME}/archive/refs/heads/{BRANCH_NAME}.zip'
GITHUB_API_URL = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/releases/latest'
GITHUB_TOKEN = "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"



class UpdateVersion:
    def __init__(self):
        self.session = requests.Session()

    def get_latest_version(self):
        response = self.session.get(VERSION_FILE_URL, verify=True)  # SSL検証を有効にする
        
        if response.status_code == 200:
            # version.pyファイルの内容を取得
            version_file_content = response.text
            print(f"Version file content:\n{version_file_content}")  # ファイル内容を出力して確認

            # __version__の値を抽出
            for line in version_file_content.splitlines():
                print(f"Line: {line}")
                if line.startswith('__version__'):
                    print("Version line found")
                    # バージョン情報を取得
                    latest_version = line.split('=')[1].strip().strip('"\'')
                    print(f"Latest Version: {latest_version}")
                    return latest_version
        else:
            print(f"Failed to fetch the version file. Status code: {response.status_code}")

        return None

    def download_and_extract_zip(self, url, extract_to='.'):
        headers = {'Authorization': f'token {GITHUB_TOKEN}'}
        response = self.session.get(url, headers=headers, verify=True)  # SSL検証を有効にする
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
        print(latest_version)
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