from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)
# captcha = ReCaptchaField(widget=ReCaptchaV3)
