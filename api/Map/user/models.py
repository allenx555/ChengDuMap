from Map import db
from .encrypt import encrypt


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    token = db.Column(db.String(255), nullable=False)
    likelist = db.Column(db.PickleType, nullable=True)
    commentlist = db.Column(db.PickleType, nullable=True)
    description = db.Column(db.String(255), nullable=True)

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
        self.phone = args['phone']
        self.password = encrypt(args['password'])
        self.is_active = True
        self.token = 'init'

        db.session.add(self)
        db.session.commit()

    def reset_password(self, new_password):
        pass
