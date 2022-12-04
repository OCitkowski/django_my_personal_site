from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls.static import static
from config import settings
from handbook.views import NoteViewSet, OwnerViewSet, SourceViewSet


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'notes', NoteViewSet)
router.register(r'owners', OwnerViewSet, 'owner_name')
router.register(r'source', SourceViewSet, 'source_name')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

handler404 = 'basis_of_project.views.custom_page_not_found_view'
# handler500 = 'basis_of_project.views.custom_error_view'
# handler403 = 'basis_of_project.views.custom_permission_denied_view'
# handler400 = 'basis_of_project.views.custom_bad_request_view'

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('', include('home_page.urls')),
    path('home/', include('home_page.urls')),
    path('aboutme/', include('about_me_page.urls')),
    path('resume/', include('resume_page.urls')),
    path('contact/', include('contact_page.urls')),
    path('api-auth/', include('rest_api.urls')),
    path('admin/', admin.site.urls),
    # re_path('^owners/(?P<username>.+)/$', OwnerViewSet.as_view()),
    # path('__debug__/', include('debug_toolbar.urls')),
    # re_path(r'^anymail/', include('anymail.urls')),#https://anymail.dev/en/stable/installation/
]

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:

    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
