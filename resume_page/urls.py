from django.urls import path
from .views import ResumeView

app_name = 'resume_page'

urlpatterns = [
    path('', ResumeView.as_view(), name='resume'),
]
