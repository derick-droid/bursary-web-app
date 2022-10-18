release: pipenv run upgrade
release: python3 manage.py migrate
web: gunicorn bursary.wsgi --log-file -