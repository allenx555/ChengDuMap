from Map import db

class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(5555), nullable=False)
    activable = db.Column(db.String(30), nullable=False)
    startdate = db.Column(db.String(50), nullable=True)
    enddate = db.Column(db.String(50), nullable=True)
    phone = db.Column(db.String(15), unique=True, nullable=True)
    x = db.Column(db.String(20), nullable=False)
    y = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    cate = db.Column(db.String(2), nullable=False)
    
    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return self.is_active

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def serialize(self, user_id):
        dicts = {}
        dicts['is_self'] = True if user_id == self.id else False
        dicts['id'] = self.id
        dicts['username'] = self.username
        dicts['email'] = self.email

        return dicts

    def save(self, args):

        self.name = args['name']
        self.description = args['description']
        self.activable = args['activable']
        self.startdate = args['startdate']
        self.enddate = args['enddate']
        self.phone = args['phone']
        self.x = args['x']
        self.y = args['y']
        self.location = args['location']
        self.cate = args['cate']

        db.session.add(self)
        db.session.commit()


    def reset_password(self, new_password):
        pass
