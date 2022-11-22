from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3
from django.shortcuts import render, HttpResponse, redirect
from django.core.mail import send_mail, EmailMessage, BadHeaderError
from config.settings import  EMAIL_HOST_PASSWORD,EMAIL_HOST_USER


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50, label='first name')
    last_name = forms.CharField(max_length=50, label='last name')
    email_address = forms.EmailField(max_length=150, label='email address')
    message = forms.CharField(widget=forms.Textarea, max_length=2000, label='message')
    captcha = ReCaptchaField(widget=ReCaptchaV3)
