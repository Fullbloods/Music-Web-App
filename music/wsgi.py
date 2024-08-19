"""
WSGI config for music project.

"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'music.settings')

application = get_wsgi_application()
