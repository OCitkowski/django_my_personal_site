from .models import Note, Owner, Source, STATUS
from rest_framework import serializers


class SourceSerializer(serializers.ModelSerializer):
    note_sources = serializers.StringRelatedField(many=True)

    class Meta:
        model = Source
        fields = '__all__'


class OwnerSerializer(serializers.ModelSerializer):
    note_owners = serializers.StringRelatedField(many=True)

    # note_owners = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Owner
        fields = '__all__'


class NoteSerializer(serializers.ModelSerializer):
    date_update = serializers.DateField(format="%Y-%m-%d", input_formats=['%Y-%m-%d', ])
    ownername = serializers.ReadOnlyField(source='owner.name')
    sourcename = serializers.ReadOnlyField(source='source.name')
    count_note = serializers.SerializerMethodField()

    class Meta:
        model = Note
        fields = ('id',
                  'owner',
                  'ownername',
                  'source',
                  'sourcename',
                  'comment',
                  'status',
                  'text',
                  'date_update',
                  'count_note')

    def get_count_note(self, instance):
        return Note.objects.all().count()
