from django.urls import path
from .views import AboutView

app_name = 'about_page'

urlpatterns = [
    path('', AboutView.as_view(), name='about'),
]
