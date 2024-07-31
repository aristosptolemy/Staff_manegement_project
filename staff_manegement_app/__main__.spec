# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['C:\\G_MyDrive\\staff_manegement_project\\staff_manegement_app\\__main__.py'],
    pathex=['C:\\G_MyDrive\\staff_manegement_project\\staff_manegement_app'],
    binaries=[('C:\\Users\\storm\\AppData\\Local\\Programs\\Python\\Python312\\python312.dll', '.')],
    datas=[
        ('config', 'config'),
        ('C:\\G_MyDrive\\staff_manegement_project\\README.md', '.'),
        ('C:\\G_MyDrive\\staff_manegement_project\\.venv\\Lib\\site-packages\\pykakasi\\data', 'pykakasi/data'),
        ('C:\\G_MyDrive\\staff_manegement_project\\.venv\\data\\address.db', 'jusho/data'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='staff_manegement',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='staff_manegement',
)