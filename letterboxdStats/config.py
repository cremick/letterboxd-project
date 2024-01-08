"""Letterboxd Stats development configuration."""

import pathlib

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
KEY = b'\x89@\xcb\x8b\xb9\x11\xb4\xc4p\xf9\xa9x`\xaat])\xa9a\xe12\xc2N\x99'
SECRET_KEY = KEY
SESSION_COOKIE_NAME = 'login'

# File Upload to var/uploads/
INSTA485_ROOT = pathlib.Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = INSTA485_ROOT/'var'/'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# Database file is var/insta485.sqlite3
DATABASE_FILENAME = INSTA485_ROOT/'var'/'insta485.sqlite3'