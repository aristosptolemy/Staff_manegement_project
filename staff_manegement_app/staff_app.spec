
block_cipher = None

a = Analysis(
    ['G:\\マイドライブ\\staff_manegement_project\\staff_manegement_app\\__main__.py'],
    pathex=[
        'G:\\マイドライブ\\staff_manegement_project\\staff_manegement_app',
        'G:\\マイドライブ\\staff_manegement_project\\.venv'
    ],
    binaries=[],
    datas=[('G:\\マイドライブ\\staff_manegement_project\\staff_manegement_app\\config\\*', 'configs'),
           ('G:\\マイドライブ\\staff_manegement_project\\staff_manegement_app\\config\\労働条件通知書(原本).xlsx', 'config'),
           ('G:\\マイドライブ\\staff_manegement_project\\staff_manegement_app\\config', 'config')],
    hiddenimports=['staff_manegement_app.GUI.gui_module', 'encodings', 'encodings.*', 'codecs'],
    hookspath=['G:\\マイドライブ\\staff_manegement_project'],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)


pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='staff_app',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    onefile=False
)

