from django.views.generic import ListView, DetailView, TemplateView
from basis_of_project.models import SiteConfiguration
from django.utils import timezone


MENU = [{'title': "Home", 'url_name': '/home'},
        {'title': "AboutMe", 'url_name': '/aboutme'},
        # {'title': "Resume", 'url_name': '/resume'},
        # {'title': "Portfolio", 'url_name': '/portfolio'},
        # {'title': "Blog", 'url_name': '/blogs'},
        # {'title': "Contact", 'url_name': '/contact'},
        ]

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