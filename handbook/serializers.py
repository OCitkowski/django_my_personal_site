from .models import Note, Owner, Source, STATUS
from rest_framework import serializers


class SourceSerializer(serializers.HyperlinkedModelSerializer):
    note_sources = serializers.StringRelatedField(many=True)

    class Meta:
        model = Source
        fields = '__all__'


class OwnerSerializer(serializers.ModelSerializer):
    # note_owners = serializers.StringRelatedField(many=True)
    note_owners = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Owner
        fields = '__all__'


class NoteSerializer(serializers.ModelSerializer):
    date_update = serializers.DateTimeField(format='%Y')

    class Meta:
        model = Note
        fields = ('id', 'owner', 'source', 'comment', 'status', 'text', 'date_update')
