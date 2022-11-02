from django.db import models
from solo.models import SingletonModel


class SiteConfiguration(SingletonModel):
    site_name_en = models.CharField(max_length=255, default='Site Name')
    site_name_ua = models.CharField(max_length=255, default='Site Name ua')

    first_name_en = models.CharField(max_length=255, default='Oleksandr')
    first_name_ua = models.CharField(max_length=255, default='Oleksandr ua')

    second_name_en = models.CharField(max_length=255, default='Tsitkovsky')
    second_name_ua = models.CharField(max_length=255, default='Tsitkovsky ua')

    href_facebook = models.CharField(max_length=255, default='https://www.facebook.com/o.citkowski/')
    href_instagram = models.CharField(max_length=255, default='https://www.instagram.com/citkowski/')
    href_github = models.CharField(max_length=255, default='https://www.github.com/OCitkowski')
    href_linkedin = models.CharField(max_length=255, default='https://www.linkedin.com/in/oleksander-citkowski-b3368015b/')

    foto = models.ImageField(verbose_name='Image', upload_to='images/%Y/%m/%d', blank=True)


    def __str__(self):
        return "Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"
        verbose_name_plural = "Site Configuration"
