from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask import url_for
import urllib

from app import app, db
from seeds import run, clear

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def seed():
    print('Seeding data...')
    run()

@manager.command
def unseed():
    print('Clearing seed data...')
    clear()

@manager.command
def routes():
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = '<{0}>'.format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.parse.unquote('{:50s} {:50s} {}'.format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print(line)

if __name__ == '__main__':
    manager.run()
