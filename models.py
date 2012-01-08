from django.core.validators import MinLengthValidator, MaxLengthValidator, validate_integer
from django.db import models

type_choice = (
    ('suggestion', 'Suggestion'),
    ('error', 'Error'),
)

class FeedBack(models.Model):
    feedback_name = models.CharField(max_length=25)
    feedback_email = models.EmailField()
    feedback_contact_number = models.CharField(max_length=15, validators=[MinLengthValidator(10), MaxLengthValidator(10),
                                                                 validate_integer])
    feedback_type = models.CharField(max_length=25, choices=type_choice, default='suggestion')
    feedback = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-post_date',)

    def __unicode__(self):
        return self.feedback_name + ' - ' + self.feedback_type
