from Map import db

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    date = db.Column(db.String(30), nullable=False)

    userid = db.Column(db.Integer, db.ForeignKey('users.id'))
    eventid = db.Column(db.Integer, db.ForeignKey('events.id'))
    user=db.relationship("User", backref=db.backref("users"))
    author=db.relationship("Event", backref=db.backref("events"))

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
