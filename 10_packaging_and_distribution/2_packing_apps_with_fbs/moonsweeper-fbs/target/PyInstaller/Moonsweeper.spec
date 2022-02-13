# -*- mode: python -*-

block_cipher = None


a = Analysis(['/home/michal/repos/tutorial_pyqt5/10_packaging_and_distribution/2_packing_apps_with_fbs/moonsweeper-fbs/src/main/python/main.py'],
             pathex=['/home/michal/repos/tutorial_pyqt5/10_packaging_and_distribution/2_packing_apps_with_fbs/moonsweeper-fbs/target/PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['/usr/local/lib/python3.6/dist-packages/fbs/freeze/hooks'],
             runtime_hooks=['/home/michal/repos/tutorial_pyqt5/10_packaging_and_distribution/2_packing_apps_with_fbs/moonsweeper-fbs/target/PyInstaller/fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Moonsweeper',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='Moonsweeper')
