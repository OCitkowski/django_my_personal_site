from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50, label='first name')
    last_name = forms.CharField(max_length=50, label='last name')
    email_address = forms.EmailField(max_length=150, label='email address')
    message = forms.CharField(widget=forms.Textarea, max_length=2000, label='message')

