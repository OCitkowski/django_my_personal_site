# django_my_personal_site
>My personal site.
___
>my comands
   1. python manage.py faker_fill_notes 1000 // create notes
   2. python manage.py faker_fill_all 1000 // create all
   3. python manage.py delete_all_data
   4. python manage.py post_all_data
 

>kill port
1. sudo lsof -t -i tcp:8000 | xargs kill -9

>Activate
1. python3 -m venv venv
2. source venv/bin/activate
3. python3 -m pip install --upgrade pip

>Installation Django
 1. pip install django==4.0.7 # Stable 3.2 # Next stable 4.2
 2. django-admin startproject config . # Create directory 'config'
 3. python manage.py migrate
 4. python manage.py makemigrations
 5. python manage.py createsuperuser #user/user ))
 6. python manage.py runserver #Starting development server

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

i had a little problem, but, i had solution:

    python manage.py migrate --run-syncdb

Save to requirements.txt

    pip freeze > requirements.txt

Created the project named by rest_api

    django-admin startapp rest_api\

Installation Django django-solo

    pip install django-solo
    https://github.com/lazybird/django-solo/blob/master/README.md



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

