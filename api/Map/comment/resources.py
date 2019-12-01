from flask_restful import Resource
from flask import request
from Map.comment.models import Comment
from flask_login import login_required, current_user


class GetEventComment(Resource):
    def post(self):
        eventid1 = request.json.get('eventid', False)
        print(eventid1)
        target = Comment.query.filter(Comment.eventid == eventid1).all()
        print(target)
        eventlist = []
        try:
            for event in target:
                dic = event.__dict__
                dic.pop('_sa_instance_state')
                eventlist.append(dic)
            return {'eventlist': eventlist}
        except:
            return {'message': 'Something went wrong'}, 500


class GetUserComment(Resource):
    @login_required
    def get(self):
        userid1 = current_user.id
        print(userid1)
        target = Comment.query.filter(Comment.userid == userid1).all()
        print(target)
        eventlist = []
        try:
            for event in target:
                dic = event.__dict__
                dic.pop('_sa_instance_state')
                eventlist.append(dic)
            return {'eventlist': eventlist}
        except:
            return {'message': 'Something went wrong'}, 500


class CommentCreate(Resource):
    @login_required
    def post(self):
        comment = Comment()
        args = {}
        args['eventid'] = request.json.get('eventid', False)
        args['userid'] = current_user.id
        args['content'] = request.json.get('content', False)
        try:
            comment.save(args)
            return {'message': 'Note was created'}
        except:
            return {'message': 'Something went wrong'}, 500