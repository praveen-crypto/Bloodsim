# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['BLOODSIM.py'],
<<<<<<< HEAD
             pathex=['C:\\Users\\Prave\\OneDrive\\Documents\\GitHub\\stenor.github.io\\Artery Tree'],
=======
             pathex=['C:\\Users\\Balaji\\Documents\\Bloodsim\\Artery Tree'],
>>>>>>> 529d64a9d26e86bd1a8251b3921bd5d2aab6b3ca
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
          name='BLOODSIM',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
<<<<<<< HEAD
          console=False , icon='BloodSim.ico')
=======
          console=True )
>>>>>>> 529d64a9d26e86bd1a8251b3921bd5d2aab6b3ca
