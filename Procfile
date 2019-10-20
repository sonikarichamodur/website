web: gunicorn mysite.wsgi
worker: celery -A mysite worker -l info
beat: celery -A mysite beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
release: python manage.py migrate
