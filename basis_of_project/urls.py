from django.urls import path
from .views import BaseView


app_name = 'base_urls'

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
]