#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install --use-pep517

python manage.py collectstatic --no-input
python manage.py migrate