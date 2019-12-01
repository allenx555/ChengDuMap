from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_login import LoginManager
from flask_cors import CORS

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config['RESTFUL_API_DOC_EXCLUDE'] = []
api = Api(app)
CORS(app, supports_credentials=True,
     allow_headers=["Content-Type", "Authorization", "Access-Control-Allow-Credentials"])
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


from Map.user.models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


import Map.user.resources, Map.event.resources, Map.comment.resources

api.add_resource(Map.user.resources.UserRegistration, '/api/register')
api.add_resource(Map.user.resources.UserLogin, '/api/login')
api.add_resource(Map.user.resources.UserLogout, '/api/logout')
api.add_resource(Map.user.resources.UserLikeList, '/api/getlikelist')
api.add_resource(Map.user.resources.UserCommentList, '/api/getcommentlist')
api.add_resource(Map.event.resources.EventList, '/api/geteventlist')
api.add_resource(Map.comment.resources.GetEventComment, '/api/geteventcomment')
api.add_resource(Map.comment.resources.CommentCreate, '/api/createcomment')
api.add_resource(Map.comment.resources.GetUserComment, '/api/getusercomment')
