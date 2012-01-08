from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.core.mail import send_mail
from django.conf import settings
from feedback.forms import FeedbackForm

def feedback_form(request):
    f_form = FeedbackForm()
    return render_to_response('feedback_form.html', locals(), context_instance = RequestContext( request ))

def submit(request):
    if request.method == 'POST':
        f_form = FeedbackForm(request.POST)
        if f_form.is_valid():
            f_obj = f_form.save()
            send_mail(
                'Feedback Submitted',
                'Thanks for submitting your suggestion.',
                settings.DEFAULT_FROM_EMAIL,
                [f_obj.feedback_email],
            )
            return HttpResponse('Thanks for submitting your suggestion.')
        else:
            error_fields = f_form.errors.keys()
            for each_field in error_fields:
                f_form.fields[each_field].widget.attrs['class'] = 'textbox_error'
    else:
        f_form = FeedbackForm()
    return render_to_response('feedback_form.html', locals(), context_instance = RequestContext( request ))