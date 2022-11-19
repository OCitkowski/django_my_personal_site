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
    subject = "Website Inquiry"

    def send_email(self):
        try:
            # print(self)
            # send_mail(self.subject, self.message, 'admin@example.com', ['admin@example.com'])
            # email = EmailMessage('Subject', 'Body', to=['o.citkowski@ukr.net'])
            # email.send()
            # subject = 'Thank you for registering to our site'
            # message = ' it  means a world to us '
            # email_from = EMAIL_HOST_USER
            # recipient_list = ['o.citkowski@gmail.com',]
            # send_mail(subject, message, email_from, recipient_list, False, auth_user=EMAIL_HOST_USER,
            #           auth_password=EMAIL_HOST_PASSWORD)
            # send_mail('subject', 'message', from_email=EMAIL_HOST_USER, recipient_list=['o.citkowski@gmail.com',])

            msg_email = EmailMessage(
                'Hello',
                'Body goes here',
                'from@example.com',
                ['to1@example.com', 'to2@example.com'],
                ['bcc@example.com'],
                reply_to=['another@example.com'],
                headers={'Message-ID': 'foo'},
            )
            msg_email.send()
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect("contact_page:contact")
        pass
# captcha = ReCaptchaField(widget=ReCaptchaV3)
