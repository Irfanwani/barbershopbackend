#!/usr/bin/env bash
# exit on error
set -o errexit

sudo apt install libpq-dev python3-dev

poetry install

python manage.py collectstatic --no-input
python manage.py migrate