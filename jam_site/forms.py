from django import forms
from django.core.validators import EmailValidator


# Create your forms here.

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(validators=[EmailValidator()])
    message = forms.CharField(widget=forms.Textarea)
    copy = forms.BooleanField(required=False)


class NewsletterForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(validators=[EmailValidator()])
    #email = forms.CharField(max_length=100)
