from django.db import models
from basis_of_project.utils import STATUS_CHOICES


class Home(models.Model):
    """ information for theme"""
    title_en = models.CharField(max_length=200, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    class Meta:
        ordering = ['title_en', 'date_update']
        verbose_name = 'Home'


    def __str__(self):
        if len(self.title_en) >= 50:
            return f"{self.title_en[:150]}..."
        else:
            return f"{self.title_en[:150]}"
