#!/bin/bash

echo "Installing requirements...💃"
python3.9 -m pip install -r requirements.txt
echo "makemigrations...💃"
python3.9 manage.py makemigrations --noinput
python3.9 manage.py makemigrations web --noinput
echo "migrate...💃"
python3.9 manage.py migrate --noinput
python3.9 manage.py migrate web --noinput
echo "collect static...💃"
python3.9 manage.py collectstatic
echo "chmod -R 755 *...💃"
chmod -R 755 media/portfolio/
