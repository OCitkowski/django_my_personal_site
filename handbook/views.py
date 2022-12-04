from .models import Note, Source, Owner
from rest_framework import viewsets, mixins
from rest_framework import permissions
from handbook.serializers import NoteSerializer, OwnerSerializer, SourceSerializer


class NoteViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = Note.objects.prefetch_related('owner').order_by('-date_update')
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]


class SourceViewSet(viewsets.ModelViewSet):
    # queryset = Source.objects.all()
    serializer_class = SourceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        http://example.com/api/v1/owners?name_request=denvercoder9
        """
        queryset = Source.objects.all()
        name_request = self.request.query_params.get('source_name')
        if name_request is not None:
            queryset = queryset.filter(name=name_request)
            print(name_request)
        return queryset


class OwnerViewSet(viewsets.ModelViewSet):
    # queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        http://example.com/api/v1/owners?name_request=denvercoder9
        """
        queryset = Owner.objects.all()
        name_request = self.request.query_params.get('owner_name')
        if name_request is not None:
            queryset = queryset.filter(name=name_request)
            print(name_request)
        return queryset
