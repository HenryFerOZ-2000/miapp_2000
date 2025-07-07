"""
WSGI config for miapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys

path = '/home/tu_usuario/miapp_2000'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'miapp.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
