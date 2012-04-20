from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers import MeetingHandler

meeting_handler = Resource(MeetingHandler)

urlpatterns = patterns('', 
    url(r'^meetings\.(?P<emitter_format>.+)', meeting_handler),
    )


