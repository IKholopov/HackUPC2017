web: gunicorn hackupc.wsgi --chdir hackupc
postdeploy: python manage.py makemigrations && python manage.py migrate