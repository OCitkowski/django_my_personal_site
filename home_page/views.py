from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

class HomeView(TemplateView):
    template_name = "home_page/base.html"
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     user_context = self.get_user_context(title='home')
    #
    #     return context | user_context
