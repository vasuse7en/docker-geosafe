"""fluentgrid URL Configuration

[...]
"""
from django.conf.urls import url, patterns
from fluentgrid.views import send_event, event_view, update_event_context

urlpatterns = patterns(
    '',
    url(
        r'^analysis/send-event/$',
        send_event,
        name='send-event'
    ),
    url(
        r'^analysis/send-event/update_event_context/',
        update_event_context,
        name='update_event_context'
    ),
    url(
        r'^analysis/open-event-modal/(?P<pk>\d+)$',
        event_view,
        name='open_event_modal'
    ),
)
