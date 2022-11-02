from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import TextAboutMe, PersonalInformation

class TextAboutMeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text')
    list_display_links = ('id', 'title', 'text')
    search_fields = ('title',)


admin.site.register(TextAboutMe, TextAboutMeAdmin)
admin.site.register(PersonalInformation, SingletonModelAdmin)
