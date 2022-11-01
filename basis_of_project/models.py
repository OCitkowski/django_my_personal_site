from django.db import models
from solo.models import SingletonModel

STATUS_CHOICES = [
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
]

MENU = [{'title': "Home", 'url_name': ''},
        {'title': "AboutMe", 'url_name': 'aboutme'},
        {'title': "Resume", 'url_name': 'resume'},
        {'title': "Portfolio", 'url_name': 'portfolio'},
        {'title': "Blog", 'url_name': 'blogs'},
        {'title': "Contact", 'url_name': 'contact'},
        ]


class SiteConfiguration(SingletonModel):
    site_name_en = models.CharField(max_length=255, default='Site Name')
    site_name_ua = models.CharField(max_length=255, default='Site Name ua')

    first_name_en = models.CharField(max_length=255, default='Oleksandr')
    first_name_ua = models.CharField(max_length=255, default='Oleksandr ua')

    second_name_en = models.CharField(max_length=255, default='Tsitkovsky')
    second_name_ua = models.CharField(max_length=255, default='Tsitkovsky ua')

    foto = models.ImageField(verbose_name='Image', upload_to='images/%Y/%m/%d', blank=True)


    def __str__(self):
        return "Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"
        verbose_name_plural = "Site Configuration"
