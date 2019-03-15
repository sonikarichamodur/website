web: gunicorn mysite.wsgi
worker: celery -A mysite worker -l info
release: python manage.py migrate
