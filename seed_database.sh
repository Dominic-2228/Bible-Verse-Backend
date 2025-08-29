#!/bin/bash

rm db.sqlite3
rm -rf ./Backend/migrations
python3 manage.py makemigrations Backend
python3 manage.py migrate
python3 manage.py migrate Backend
python3 manage.py loaddata users
python3 manage.py loaddata posts
python3 manage.py loaddata comments
python3 manage.py loaddata userlikes
python3 manage.py loaddata notes