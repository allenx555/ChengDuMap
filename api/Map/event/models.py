from Map import db

class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    startdate = db.Column(db.Date, nullable=True)
    enddate = db.Column(db.Date, nullable=True)
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

        db.session.add(self)
        db.session.commit()

    def reset_password(self, new_password):
        pass
