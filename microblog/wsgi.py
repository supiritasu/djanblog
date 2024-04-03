"""
WSGI config for microblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from pathlib import Path

from django.core.wsgi import get_wsgi_application
from wsgi_basic_auth import BasicAuth
import dotenv

# .envファイルから環境変数を読み込む
BASE_DIR = Path(__file__).resolve().parent.parent
dotenv.load_dotenv(os.path.join(BASE_DIR, ".env"))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'microblog.settings')
BASIC_AUTH_USERNAME = os.getenv("BASIC_AUTH_USERNAME")
BASIC_AUTH_PASSWORD = os.getenv("BASIC_AUTH_PASSWORD")
# Basic認証を設定
application = BasicAuth(get_wsgi_application())

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'microblog.settings')

application = get_wsgi_application()
app = application