from django import forms
from feedback.models import FeedBack

class FeedbackForm(forms.ModelForm):

    def __init__( self, *args, **kwargs ):
        super( forms.ModelForm, self ).__init__( *args, **kwargs )

        self.fields['feedback_contact_number'].widget.attrs['class'] = 'textbox'
        self.fields['feedback_contact_number'].label = 'Contact No'

        self.fields['feedback_name'].widget.attrs['class'] = 'textbox'
        self.fields['feedback_name'].label = 'Name'

        self.fields['feedback_email'].widget.attrs['class'] = 'textbox'
        self.fields['feedback_email'].label = 'Email'

        self.fields['feedback_type'].widget.attrs['class'] = 'dropdown'
        self.fields['feedback_type'].label = 'Type'

        self.fields['feedback'].widget.attrs['class'] = 'textbox'

    class Meta:
        model = FeedBack