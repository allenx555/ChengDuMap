from flask_restful import Resource
from Map.event.models import Event


class EventList(Resource):
    def get(self):
        events = Event()
        events = events.query.all()
        eventlist = []
        for event in events:
            dic = event.__dict__
            dic.pop('_sa_instance_state')
            eventlist.append(dic)
        print(eventlist)
        if eventlist:
            return {'eventlist': eventlist}
        else:
            return {'message': 'Something went wrong'}, 500
