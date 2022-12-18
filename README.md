# django_my_personal_site
My personal site.


kill port

    sudo lsof -t -i tcp:8000 | xargs kill -9

Activate

    python3 -m venv venv
    source venv/bin/activate
    python3 -m pip install --upgrade pip

Installation Django

    pip install django==4.0.7 # Stable 3.2 # Next stable 4.2
    django-admin startproject config . # Create directory 'config'
    python manage.py migrate
    python manage.py makemigrations
    python manage.py createsuperuser #user/user ))
    python manage.py runserver #Starting development server

___
> **************** shell *************************  

    1. python manage.py shell
    2. importing the function from utils
    from django.core.management.utils import get_random_secret_key
    3. generating and printing the SECRET_KEY
    print(get_random_secret_key())
___


Installation Django REST framework

    pip install djangorestframework
    pip install markdown # Markdown support for the browsable AP
    pip install django-filter # Filtering support

Save to requirements.txt

    pip freeze > requirements.txt

Created the project named by rest_api

    django-admin startapp rest_api\

Installation Django django-solo

    pip install django-solo
    https://github.com/lazybird/django-solo/blob/master/README.md

i had a little problem, but, i had solution:

    python manage.py migrate --run-syncdb

install django-debug-toolbar

    https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
    python -m pip install django-debug-toolbar

icon for the Services

    http://www.appstraptheme.com/appstrap3.3.2/theme/elements-icons-linearicons.html

template tags and filters

    https://docs.djangoproject.com/en/dev/ref/templates/builtins/?from=olddocs#safe

recapcha v.3
    
    https://developers.google.com/recaptcha/docs/display

anymail 

    https://anymail.dev/en/stable/installation/

python-dotenv
    
    pip install python-dotenv

