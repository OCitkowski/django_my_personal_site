from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls.static import static
from config import settings


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

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

handler404 = 'basis_of_project.views.custom_page_not_found_view'
# handler500 = 'basis_of_project.views.custom_error_view'
# handler403 = 'basis_of_project.views.custom_permission_denied_view'
# handler400 = 'basis_of_project.views.custom_bad_request_view'

urlpatterns = [
    path('', include(router.urls)),
    path('home/', include('home_page.urls')),
    path('aboutme/', include('about_me_page.urls')),
    path('api-auth/', include('rest_api.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
]

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:

    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]