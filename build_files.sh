#!/bin/bash

echo "Installing requirements..."
python3.9 -m pip install -r requirements.txt
echo "makemigrations..."
python3.9 manage.py makemigrations web --noinput
python3.9 manage.py migrate web --noinput
echo "collect static..."
python3.9 manage.py collectstatic
