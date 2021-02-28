# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['whale.py'],
             pathex=['D:\\w'],
             binaries=[],
             datas=['36_1.jpg','37_1.jpg','38_1.jpg','39_1.jpg','4_1.jpg','40_1.jpg','41_1.jpg','42_1.jpg','5_1.jpg','6_1.jpg','7_1.jpg','8_1.jpg','9_1.jpg','about.txt','click.wav','correct.wav','firstpage.jpg',
			'firstpage.png',
			'list.txt',
			'page1.wav',
			'page2.mp3',
			'page2.wav'.
			'right.png'.
			'TaipeiSansTCBeta-Bold.ttf',
			'whale.ico',
			'whale.py',
			'whale_name.txt',
			'wrong.png',
			'wrong.wav'],
             hiddenimports=['cython','sklearn','sklearn.ensemble','sklearn.neighbors.typedefs','sklearn.neighbors.quad_tree','sklearn.tree._utils','sklearn.utils._cython_blas'],
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
          [],
          exclude_binaries=True,
          name='whale',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='whale')
