#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py migrate
python manage.py seed --if-empty
python manage.py collectstatic --no-input
