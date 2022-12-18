from django.contrib import admin
from .models import Owner, Source, Note, TypeKey, Key


@admin.register(Key)
class KeyAdmin(admin.ModelAdmin):
    list_display = ('id', 'link', 'type_key')
    list_display_links = ('id', 'link', 'type_key')
    search_fields = ('link',)


@admin.register(TypeKey)
class TypeKeyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


@admin.register(Owner)
class TextAboutMeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'comment')
    list_display_links = ('id', 'name', 'comment')
    search_fields = ('name',)


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'comment')
    list_display_links = ('id', 'name', 'comment')
    search_fields = ('name',)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'source', 'text', 'comment', 'date_update', 'status')
    list_display_links = ('id', 'owner', 'source', 'text', 'comment', 'date_update', 'status')
    search_fields = ('owner', 'source', 'status', 'date_update')
