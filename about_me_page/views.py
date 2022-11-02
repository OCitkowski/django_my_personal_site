from django.views.generic import ListView, DetailView, TemplateView
from basis_of_project.models import SiteConfiguration
from basis_of_project.utils import MENU
from django.utils import timezone
# from .models import About


class AboutView(ListView):

    model = SiteConfiguration
    template_name = 'about_me_page/about.html'
    context_object_name = 'about'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['home'] = Home.objects.filter(status='p')
        context['first'] = SiteConfiguration.objects.all().first()
        context['now'] = timezone.now()
        context['menu'] = MENU
        return context
