from django.contrib import admin
from feedback.models import FeedBack

class AdminFeddbackClass(admin.ModelAdmin):
    list_display = ('feedback_name', 'feedback_type', 'post_date')
    list_filter = ('feedback_type',)
    readonly_fields = ('feedback_name', 'feedback_email', 'feedback_contact_number', 'feedback_type',
        'post_date', 'feedback')

admin.site.register(FeedBack, AdminFeddbackClass)
