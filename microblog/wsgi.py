"""
WSGI config for microblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from wsgi_basic_auth import BasicAuth
import dotenv
import environ
from pathlib import Path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'microblog.settings')

# Basic認証を設定
application = BasicAuth(get_wsgi_application())
# application = BasicAuth(application)


# .envファイルから環境変数を読み込む
BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env"))
dotenv.load_dotenv()

# 環境変数WSGI_AUTH_CREDENTIALSから認証情報を取得して分割する
auth_credentials = os.getenv('WSGI_AUTH_CREDENTIALS').split(':')
username = auth_credentials[0]
password = auth_credentials[1]

application = get_wsgi_application()
application = BasicAuth(application, username=username, password=password)
