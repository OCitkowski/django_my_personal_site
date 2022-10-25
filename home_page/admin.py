from django.contrib import admin
from .models import Home


@admin.action(description='Mark selected blog as published')
def make_published(modeladmin, request, queryset):
    queryset.update(status='p')


@admin.action(description='Mark selected blog as draft')
def make_draft(modeladmin, request, queryset):
    queryset.update(status='d')


@admin.action(description='Mark selected blog as withdrawn')
def make_withdrawn(modeladmin, request, queryset):
    queryset.update(status='w')


class HomeAdmin(admin.ModelAdmin):
    actions = [make_published, make_draft, make_withdrawn]
    prepopulated_fields = {"title_en": ('title_ua', 'date_update')}


admin.site.register(Home, HomeAdmin)
