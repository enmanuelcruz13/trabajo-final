#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py migrate
python manage.py seed  # force re-seed with corrected Spanish IDs
python manage.py collectstatic --no-input
