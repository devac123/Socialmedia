import django
import os
from channels.routing import get_default_application
os.environ.setdefault("DJANGO_SETTING_MODULE","socialmedia.settings")
django.setup()
application = get_default_application()