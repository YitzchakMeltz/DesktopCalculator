# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['C:\\Users\\hmeltz\\Documents\\GitHub\\DesktopCalculator\\DesktopCalculatorGUI_1.1.0.py'],
             pathex=['C:\\Users\\hmeltz\\AppData\\Local\\Programs\\Python\\Python39\\Scripts'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='DesktopCalculatorGUI_1.1.0',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='C:\\Users\\hmeltz\\Documents\\GitHub\\DesktopCalculator\\Logos\\CalculatorLogo(150p)_1.0.0.ico')
