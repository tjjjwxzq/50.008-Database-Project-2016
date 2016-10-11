from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db
from seeds import customer

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def seed():
    result = db.engine.execute(customer)

if __name__ == '__main__':
    manager.run()
