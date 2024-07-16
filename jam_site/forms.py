from django import forms
from django.core.validators import EmailValidator

# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
# from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions



# Create your forms here.

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(validators=[EmailValidator()])
    message = forms.CharField(widget=forms.Textarea)
    copy = forms.BooleanField(required=False)


class NewsletterForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(validators=[EmailValidator()])