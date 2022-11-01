from django.views.generic import ListView, DetailView, TemplateView
from basis_of_project.models import SiteConfiguration
from basis_of_project.utils import MENU
from django.utils import timezone


class HomeView(ListView):

    model = SiteConfiguration
    template_name = 'home_page/home.html'
    context_object_name = 'basis'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first'] = SiteConfiguration.objects.all().first()
        context['now'] = timezone.now()
        context['menu'] = MENU
        return context