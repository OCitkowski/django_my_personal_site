
___
1. Source code: /home/ocitkowski/django_my_personal_site
2. Working directory: /home/ocitkowski/
3. WSGI configuration file: /var/www/ocitkowski_pythonanywhere_com_wsgi.py
4. Python version: 3.10
___

/media 	    /home/ocitkowski/django_my_personal_site/media 
/static 	/home/ocitkowski/django_my_personal_site/static

___


# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys
#
## assuming your django settings file is at '/home/ocitkowski/mysite/mysite/settings.py'
## and your manage.py is is at '/home/ocitkowski/mysite/manage.py'
path = '/home/ocitkowski/django_my_personal_site/'
if path not in sys.path:
    sys.path.append(path)
#
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
#
## then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


___

git clone https://github.com/OCitkowski/django_my_personal_site.git
mkvirtualenv --python=/usr/bin/python3.10 mysite-virtualenv