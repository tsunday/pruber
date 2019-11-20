#!/usr/bin/env bash

python manage.py migrate
python manage.py loaddata rooms.yaml bands.yaml schedule.yaml
python manage.py runserver 0.0.0.0:9000