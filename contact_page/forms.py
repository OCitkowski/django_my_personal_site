from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50, label='first name')
    last_name = forms.CharField(max_length=50, label='last name')
    email_address = forms.EmailField(max_length=150, label='email address')
    message = forms.CharField(widget=forms.Textarea, max_length=2000, label='message')
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

