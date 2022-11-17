from .forms import ContactForm
from django.shortcuts import render, HttpResponse
from config.settings import RECAPTCHA_PRIVATE_KEY
from django.core.mail import send_mail, BadHeaderError


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
                return HttpResponse('Ok')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

    form = ContactForm()
    return render(request, "contact_page/contact.html", {'form': form, 'recaptcha_site_key': RECAPTCHA_PRIVATE_KEY})

