from django.urls import path, include
from handbook.views import NoteViewSet, OwnerViewSet, SourceViewSet, TypeKeyViewSet, KeyViewSet
from rest_api.views import UserViewSet, HomeViewSet
from rest_framework import routers

app_name = 'rest_api'

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'notes', NoteViewSet)
router.register(r'owners', OwnerViewSet, 'owner_name')
router.register(r'source', SourceViewSet, 'source_name')
router.register(r'type_key', TypeKeyViewSet, 'type_key')
router.register(r'key', KeyViewSet)
router.register(r'home', HomeViewSet, 'home_api')

urlpatterns = [

    path('', include(router.urls)),

]
