from .forms import ContactForm

from config.settings import RECAPTCHA_PRIVATE_KEY
# from myapp.forms import ContactForm
from django.views.generic.edit import FormView
from basis_of_project.utils import MENU
from django.utils import timezone
from basis_of_project.models import SiteConfiguration

class ContactFormView(FormView):
    template_name = 'contact_page/contact.html'
    form_class = ContactForm
    success_url = '/contact/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first'] = SiteConfiguration.objects.all().first()
        context['now'] = timezone.now()
        context['menu'] = MENU
        return context

#
# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = "Website Inquiry"
#             body = {
#                 'first_name': form.cleaned_data['first_name'],
#                 'last_name': form.cleaned_data['last_name'],
#                 'email': form.cleaned_data['email_address'],
#                 'message': form.cleaned_data['message'],
#             }
#             message = "\n".join(body.values())
#
#             try:
#                 # send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
#                 # return HttpResponse('Ok')
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#     form = ContactForm()
#     return render(request, "contact_page/contact.html", {'form': form, 'recaptcha_site_key': RECAPTCHA_PRIVATE_KEY})

