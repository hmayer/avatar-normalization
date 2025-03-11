import shutil
import tempfile
import atexit
from flask import Flask

def graceful_shutdown():
    shutil.rmtree(tempdir)

atexit.register(graceful_shutdown)

app = Flask('avatar-normalizer')

tempdir = tempfile.mkdtemp(
    prefix='avatar-normalizer-',
    dir='/tmp'
)

from src.Avatar.Controllers import AvatarController
