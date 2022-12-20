from .models import Note, Owner, Source, Key, TypeKey
from rest_framework import serializers


class TypeKeySerializer(serializers.ModelSerializer):
    type_key = serializers.StringRelatedField(many=True)

    class Meta:
        model = TypeKey
        fields = '__all__'


class KeySerializer(serializers.ModelSerializer):
    type_key_name = serializers.ReadOnlyField(source='type_key.name')

    class Meta:
        model = Key
        # fields = '__all__'
        fields = ('id',
                  'link',
                  'type_key_name',
                  'type_key')


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
    keylink = serializers.ReadOnlyField(source='key.link')
    type_key = serializers.ReadOnlyField(source='key.type_key.name')
    count_note = serializers.SerializerMethodField()

    class Meta:
        model = Note
        fields = ('id',
                  'owner',
                  'ownername',
                  'source',
                  'sourcename',
                  'text',
                  'comment',
                  'keylink',
                  'type_key',
                  'key',
                  'status',
                  'date_update',
                  'count_note',
                  )

    def get_count_note(self, instance):
        return Note.objects.all().count()
