from flask_restful import Resource
from flask import session, request
from Map.user.models import User
from flask_login import login_user, logout_user, login_required, current_user
from Map.user.encrypt import decrypt


class UserRegistration(Resource):
    def post(self):
        if User.query.filter_by(phone=request.json.get('phone', False)).first():
            return {'message': 'User {} already exists'.format(request.json.get('phone', False))}

        user = User()
        args = {}
        args['phone'] = request.json.get('phone', False)
        args['password'] = request.json.get('password', False)
        try:
            user.save(args)
            return {
                'message': 'User {} was created'.format(request.json.get('phone', False)),
            }
        except:
            return {'message': 'Something went wrong'}, 500


class UserLogin(Resource):
    def post(self):
        user = User.query.filter_by(phone=request.json.get("phone", False)).first()
        if user:
            if (request.json.get("password", False), user.password):
                login_user(user)

                return {'token': session['_id']}, 200
            else:
                return {'message': 'password is wrong'}, 400
        else:
            return {'message': 'no user'}, 400


class UserLogout(Resource):
    @login_required
    def get(self):
        logout_user()
        return {'status': 200}


class UserLikeList(Resource):
    @login_required
    def get(self):
        likelist = current_user.likelist.all()
        print(current_user.likelist)
        if likelist:
            return {'likelist': likelist}
        else:
            return {'message': 'Something went wrong'}, 500


class UserCommentList(Resource):
    @login_required
    def get(self):
        commentlist = current_user.commentlist.all()
        print(current_user.commentlist)
        if commentlist:
            return {'commentlist': commentlist}
        else:
            return {'message': 'Something went wrong'}, 500
