from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import TextAboutMe, PersonalInformation, Services

@admin.register(TextAboutMe) # it the variant 1
class TextAboutMeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text')
    list_display_links = ('id', 'title', 'text')
    search_fields = ('title',)


@admin.register(Services) # it the variant 1+
class ServicesAdmin(admin.ModelAdmin):
    pass

# admin.site.register(TextAboutMe, TextAboutMeAdmin) # it the variant 2
admin.site.register(PersonalInformation, SingletonModelAdmin)
# admin.site.register(Services) # it the variant 2
