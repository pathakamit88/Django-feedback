from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('feedback.views',
    url( r'^feedback_form/$', 'feedback_form'),
    url( r'^submit/$', 'submit'),
)