from flask_script import Manager
from Map import app
from Map import db
from Map.user.models import User


manager = Manager(app)


@manager.command
def db_create():
    try:
        db.create_all()
        print('you had create db')
    except:
        print('error!')

    user = User()
    args = {}
    args['phone'] = '1234567891011'
    args['password'] = '123456'

    try:
        user.save(args)
    except:
        print(args['username'], ' load error!')

    print('load over!')


if __name__ == '__main__':
    manager.run()
