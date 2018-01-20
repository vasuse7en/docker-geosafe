"""fluentgrid URL Configuration

[...]
"""
from django.conf.urls import url, patterns
from fluentgrid.views import send_event

urlpatterns = patterns(
    '',
    url(
        r'^analysis/send-event/',
        send_event,
        name='send-event'
    ),
)