update

    apt-get update
    apt-get upgrade
    sudo apt update 
    sudo apt upgrade -y

install

    sudo apt-get install package-name

clean

    sudo apt-get autoremove
    sudo apt autoclean

vboxsf

    sudo usermod -a -G vboxsf fox

kill
    
    sudo lsof -t -i tcp:8000 | xargs kill -9

venv

    python -m venv venv
    source venv/bin/activate  (deactivate)
    pip install virtualenv (mind)
    virtualenv venv

pip

    python -m pip install --upgrade pip

django

    pip install django
    django-admin startproject config .

    python manage.py migrate 
    python manage.py migrate --run-syncdb
    python manage.py makemigrations

    python manage.py createsuperuser
    python manage.py runserver    

    django-admin startapp blog  *****

    python manage.py shell
    python manage.py collectstatic

apps

    python -m pip install Pillow

requirements

    pip freeze > requirements.txt 
    pip install -r requirements.txt
    pip uninstall requirements.txt


token

    from rest_framework.authtoken.models import Token
        token = Token.objects.create(user=fox)
    print(token.key)
