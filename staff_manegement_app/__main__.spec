# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['G:\\マイドライブ\\staff_manegement_project\\staff_manegement_app\\__main__.py'],
    pathex=['G:\\マイドライブ\\staff_manegement_project\\staff_manegement_app'],
    binaries=[('C:\\Users\\storm\\AppData\\Local\\Programs\\Python\\Python312\\python312.dll', '.')],
    datas=[
        ('config', 'config')
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
    console=False,
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