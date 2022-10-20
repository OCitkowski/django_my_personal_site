# django_my_personal_site
My personal site.

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

Installation Django REST framework

    pip install djangorestframework
    pip install markdown # Markdown support for the browsable AP
    pip install django-filter # Filtering support

Save to requirements.txt

    pip freeze > requirements.txt

Created the project named by rest_api

    django-admin startapp rest_api
