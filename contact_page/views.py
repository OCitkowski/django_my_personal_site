from .forms import ContactForm
from django.views.generic.edit import FormView
from basis_of_project.utils import MENU
from django.utils import timezone
from basis_of_project.models import SiteConfiguration
from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import HttpResponse, redirect


class ContactFormView(FormView):
    template_name = 'contact_page/contact.html'
    form_class = ContactForm
    success_url = '/contact/'

    def form_valid(self, form):
        self.send_email(form)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first'] = SiteConfiguration.objects.all().first()
        context['now'] = timezone.now()
        context['menu'] = MENU
        return context

    def send_email(self, form):
        try:
            first_name = form.cleaned_data.get('first_name')
            # first_name = self.request.POST.get('first_name')
            last_name = self.request.POST.get('last_name')
            email_address = self.request.POST.get('email_address')
            message = self.request.POST.get('message')

            recipient_list = [email_address, ]
            msg_email = EmailMessage(
                subject=f'Hello {first_name} {last_name}',
                body=message,
                to=recipient_list
            )
            msg_email.send()
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect("contact_page:contact")
        pass



