from flask_script import Manager
from Map import app
from Map import db
from Map.user.models import User
from Map.event.models import Event


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
    args['phone'] = '12345678910'
    args['password'] = '123456'
    
    event = Event()
    args2 = {}

    args2['name'] = '知更鸟动漫游戏交流展'
    args2['activable'] = '在售中'
    args2['startdate'] = '2020.01.01 09:30'
    args2['enddate'] = ''
    args2['phone'] = ''
    args2['x'] = '104.081785'
    args2['y'] = '30.420097'
    args2['location'] = '中国西部国际博览城'
    args2['cate'] = '2'
    args2['description'] = '#知更鸟动漫游戏交流展#我们来了！为所有喜爱ACG的'


    try:
        user.save(args)
    except:
        print(args['username'], ' load error!')

    try:
        event.save(args2)
    except:
        print(args2['name'],'load error!')

    print('load over!')


if __name__ == '__main__':
    manager.run()
