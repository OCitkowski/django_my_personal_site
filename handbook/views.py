from .models import Note, Source, Owner, Key, TypeKey
from rest_framework import viewsets, mixins
from rest_framework import permissions
from handbook.serializers import NoteSerializer, OwnerSerializer, SourceSerializer, KeySerializer, TypeKeySerializer


# class NoteViewSet(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   mixins.UpdateModelMixin,
#                   mixins.DestroyModelMixin,
#                   viewsets.GenericViewSet):
#     queryset = Note.objects.prefetch_related('owner').order_by('-date_update')
#     serializer_class = NoteSerializer
#     permission_classes = [permissions.IsAuthenticated]

class NoteViewSet(viewsets.ModelViewSet):
    # {
    #     "id": 1,
    #     "owner": 1,
    #     "ownername": "Alex Willis",
    #     "source": 1,
    #     "sourcename": "brittany04@example.net",
    #     "text": "KtqLTAyOVCnXGqQEZILc",
    #     "comment": "People affect some professional soon budget research leader feeling writer.",
    #     "keylink": "knight.com",
    #     "type_key": "Ameliorated context-sensitive software",
    #     "key": 1,
    #     "status": "('A', 'Active')",
    #     "date_update": "2022-12-28",
    #     "count_note": 1010
    # },

    # queryset = Note.objects.prefetch_related('owner').order_by('-date_update')
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        http://example.com/api/v1/notes?name_request=denvercoder9
        """
        queryset = Note.objects.all()

        value_source = self.request.query_params.get('source')
        value_owner = self.request.query_params.get('owner')


        for params in self.request.query_params:
            if params == 'source':
                print(f'{value_source} - source')
                queryset = queryset.filter(source=value_source)
            if params == 'owner':
                print(f'{value_owner} - owner')
                queryset = queryset.filter(owner=value_owner)

        return queryset


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


class TypeKeyViewSet(viewsets.ModelViewSet):
    serializer_class = TypeKeySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        http://example.com/api/v1/owners?name_request=denvercoder9
        """
        queryset = TypeKey.objects.all()
        name_request = self.request.query_params.get('type_key')
        if name_request is not None:
            queryset = queryset.filter(name=name_request)
            print(name_request)
        return queryset


class KeyViewSet(viewsets.ModelViewSet):
    queryset = Key.objects.all()
    serializer_class = KeySerializer
    permission_classes = [permissions.IsAuthenticated]
