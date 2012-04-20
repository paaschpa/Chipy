from piston.handler import BaseHandler
from meetings.models import Meeting

class MeetingHandler(BaseHandler):
  allowed_methods = ('GET',)
  model = Meeting
  fields = ('when', 'which', ('venue', ('name',)), ('topic_set', ('title', 'description', 'length', 'start_time', ('by', ('name',)))))

  def read(self, request, meeting_id=None):
    print request
    base = Meeting.objects
    if meeting_id:
      meeting_json = []
      meeting = base.get(pk=meeting_id)
      meeting_json.append({'meeting': meeting, 'topics': meeting.topic_set.all()})
      return meeting_json
    else:
      return Meeting.objects.all()
