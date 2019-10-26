#!/usr/bin/env bash

python manage.py migrate
python manage.py loaddata rooms.yaml
python runserver 0.0.0.0:8000