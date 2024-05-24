起動用
python -m staff_manegement_app

pyinstaller --onefile "__main__.py"

pyinstaller --onefile --windowed "G:\マイドライブ\staff_manegement_project\staff_manegement_app\__main__.py"
pyinstaller --windowed "G:\マイドライブ\staff_manegement_project\staff_manegement_app\__main__.py"

$ pyinstaller __main__.spec

pyinstaller --onefile --windowed --add-binary "C:\Users\storm\AppData\Local\Programs\Python\Python312\python312.dll;." "G:\マイドライブ\staff_manegement_project\staff_manegement_app\__main__.py"