from django.views.generic import ListView, DetailView, TemplateView

class BaseView(TemplateView):
    template_name = "basis_of_project/index.html"