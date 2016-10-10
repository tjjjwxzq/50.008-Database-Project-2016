# 50.008 Database Bookstore

A simple bookstore application buildt with Flask and PostgreSQL.

## System requirements

You should have Python 3.x with pip and PostgreSQL 9.4 or above

## Setting up

Get autoenv

```
sudo pip install autoenv
```

Activate the virtual environment and set necessary environment variables

```
cd ..
source `which activate.sh`
cd project_directory
```

Ensure all required packages are installed

```
pip install -r requirements.txt
```

Create the database

```
psql
# create database database_project_bookstore
\l
```

Run migrations and seed data

```
python manage.py db upgrade
python manage.py seed
```

Run the server

```
flask run
```
