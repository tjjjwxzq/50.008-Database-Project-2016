# 50.008 Database Bookstore

A simple bookstore application buildt with Flask and PostgreSQL.

## System requirements

You should have Python 3.x with pip and PostgreSQL 9.4 or above

## Setting up

Get virtualenv and autoenv

```
sudo pip install virtualenv
sudo pip install autoenv
```

Set up the virtual environment. In your project directory:

```
virtualenv venv
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

## Contributing

Follow the GitHub workflow. Push your work to a separate branch, and let others know that your code is awaiting review. Once your code has passed review, squash merge it into master and delete the branch.

Name your branch meaningfully, according to what you are implementing in the branch.
Let's follow the following naming conventions:

```
featuer/some-feature
bugfix/some-bug
enhance/some-enhancement
```

Remember to always to pull the latest updated version of master before starting on a new branch, and checkout your new branch from the latest master. NEVER PUSH STRAIGHT TO MASTER.
