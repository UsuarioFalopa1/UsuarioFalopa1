# django-todo-react
django + postgres + react

Tutorial:
https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react

Add postgres db (backend/settings.py): 

DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'testPostgres',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST' : 'localhost',
        'PORT': '5432'
        }
