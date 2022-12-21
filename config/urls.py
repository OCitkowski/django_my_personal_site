from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from config import settings
from rest_framework.authtoken import views

handler404 = 'basis_of_project.views.custom_page_not_found_view'
# handler500 = 'basis_of_project.views.custom_error_view'
# handler403 = 'basis_of_project.views.custom_permission_denied_view'
# handler400 = 'basis_of_project.views.custom_bad_request_view'

urlpatterns = [
    path('api/token_auth/', views.obtain_auth_token, name='token_auth'),
    path('api/v1/', include('rest_api.urls'), name='api_v1'),
    path('home/', include('home_page.urls')),
    path('', include('home_page.urls')),
    path('aboutme/', include('about_me_page.urls')),
    path('resume/', include('resume_page.urls')),
    path('contact/', include('contact_page.urls')),
    path('admin/', admin.site.urls),

]

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:

    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
