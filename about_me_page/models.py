from django.db import models
from solo.models import SingletonModel


class PersonalInformation(SingletonModel):
    name = models.CharField(max_length=255, default='-----')
    age = models.CharField(max_length=255, default='-----')
    residence = models.CharField(max_length=255, default='-----')
    first_name = models.CharField(max_length=255, default='-----')
    second_name = models.CharField(max_length=255, default='-----')

    address = models.CharField(max_length=255, default='-----')
    email = models.EmailField(max_length=255, default='-----')
    phone = models.CharField(max_length=255, default='-----')
    freelance = models.CharField(max_length=255, default='-----')

    resume = models.FileField(upload_to='uploads/%Y/%m/%d/')

    def __str__(self):
        return "Personal Information"

    class Meta:
        verbose_name = "Personal Information"
        verbose_name_plural = "Personal Information"


class TextAboutMe(models.Model):
    title = models.CharField(max_length=100, default='About Me.')
    text = models.TextField(max_length=1000, default='-----')

    def __str__(self):
        return "About me"

    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"


class Services(models.Model):
    title = models.CharField(max_length=100, default='Web Development')
    text = models.TextField(max_length=1000,
                            default='Amet aspernatur delectus maxime ducimus similique Ratione asperiores corporis provident aut libero.')
    icon_text = models.TextField(max_length=1000, default='<i class="lnr lnr-laptop-phone">')

    def __str__(self):
        return "Services"

    class Meta:
        verbose_name = "Services"
        verbose_name_plural = "Services"
