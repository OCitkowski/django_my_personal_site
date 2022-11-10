from django.views.generic import ListView, DetailView, TemplateView
from basis_of_project.models import SiteConfiguration
from basis_of_project.utils import MENU
from django.utils import timezone
from .models import Experience, Education, Skills


class ResumeView(ListView):

    model = SiteConfiguration
    template_name = 'resume_page/resume.html'
    context_object_name = 'basis'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['experience'] = Experience.objects.filter(status='p')
        context['education'] = Education.objects.filter(status='p')
        context['skills'] = Skills.objects.filter(status='p')

        context['first'] = SiteConfiguration.objects.all().first()
        context['now'] = timezone.now()
        context['menu'] = MENU
        return context
