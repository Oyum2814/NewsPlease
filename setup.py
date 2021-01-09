"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2exe
"""
from distutils.core import setup
import py2app

APP = ['Np.py']
DATA_FILES = []
OPTIONS = {
    'iconfile':'Logo.icns',
    'argv_emulation':True,
    'packages':['py2app','requests','pandas']
}
setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app','requests','urllib3','numpy','pandas'],
)
