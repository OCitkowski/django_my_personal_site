from django.contrib import admin
from .models import Experience, Education, Skills


@admin.action(description='Mark selected blog as published')
def make_published(modeladmin, request, queryset):
    queryset.update(status='p')


@admin.action(description='Mark selected blog as draft')
def make_draft(modeladmin, request, queryset):
    queryset.update(status='d')


@admin.action(description='Mark selected blog as withdrawn')
def make_withdrawn(modeladmin, request, queryset):
    queryset.update(status='w')


class ExperienceAdmin(admin.ModelAdmin):
    actions = [make_published, make_draft, make_withdrawn]

class EducationAdmin(admin.ModelAdmin):
    actions = [make_published, make_draft, make_withdrawn]

class SkillsAdmin(admin.ModelAdmin):
    actions = [make_published, make_draft, make_withdrawn]

admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin),
admin.site.register(Skills, SkillsAdmin)
