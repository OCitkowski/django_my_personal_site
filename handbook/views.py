from .models import Note, Source, Owner
from rest_framework import viewsets, mixins
from rest_framework import permissions
from handbook.serializers import NoteSerializer, OwnerSerializer, SourceSerializer


class NoteViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    queryset = Note.objects.prefetch_related('owner').order_by('-date_update')
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    permission_classes = [permissions.IsAuthenticated]


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    permission_classes = [permissions.IsAuthenticated]
