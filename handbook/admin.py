from django.contrib import admin
from .models import Owner, Source, Note


@admin.register(Owner)
class TextAboutMeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'comment')
    list_display_links = ('id', 'name', 'comment')
    search_fields = ('name',)


@admin.register(Source)
class TextAboutMeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'comment')
    list_display_links = ('id', 'name', 'comment')
    search_fields = ('name',)


@admin.register(Note)
class TextAboutMeAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'source', 'text', 'comment', 'date_update', 'status')
    list_display_links = ('id', 'owner', 'source', 'text', 'comment', 'date_update', 'status')
    search_fields = ('owner', 'source', 'status', 'date_update')
