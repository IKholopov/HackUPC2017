web: gunicorn hackupc.wsgi --chdir hackupc
postdeploy: cd hackups && python manage.py makemigrations && python manage.py migrate