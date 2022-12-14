from django.db import models
from basis_of_project.utils import STATUS_CHOICES
from django.utils.timezone import now


class Experience(models.Model):
    title = models.CharField(max_length=200, unique=True)
    company = models.CharField(max_length=200, unique=True)
    text = models.TextField()
    date_start = models.DateField(default=now)
    date_end = models.DateField(default=now)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)


    class Meta:
        ordering = ['title', 'company', 'date_start', 'date_end', 'text', 'status']
        verbose_name = 'Experience'

    def date_start_published(self):
        return self.date_start.strftime('%Y')

    def date_end_published(self):
        return self.date_end.strftime('%Y')

    def __str__(self):
        if len(self.title) >= 50:
            return f"{self.title[:150]}..."
        else:
            return f"{self.title[:150]}"


class Education(models.Model):
    title = models.CharField(max_length=200, unique=True)
    place = models.CharField(max_length=200, unique=True)
    text = models.TextField()
    date_start = models.DateField(default=now)
    date_end = models.DateField(default=now)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)


    class Meta:
        ordering = ['title', 'place', 'date_start', 'date_end', 'text', 'status']
        verbose_name = 'Education'

    def date_start_published(self):
        return self.date_start.strftime('%Y')

    def date_end_published(self):
        return self.date_end.strftime('%Y')

    def __str__(self):
        if len(self.title) >= 50:
            return f"{self.title[:150]}..."
        else:
            return f"{self.title[:150]}"

class Skills(models.Model):
    title = models.CharField(max_length=200, unique=True)
    level = models.PositiveSmallIntegerField(default=50)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)


    class Meta:
        ordering = ['title', 'level', 'status']
        verbose_name = 'Skills'


    def __str__(self):
        if len(self.title) >= 50:
            return f"{self.title[:150]}..."
        else:
            return f"{self.title[:150]}"