import datetime
from django.db import models

STATUS = [
    ('A', 'Active'),
    ('C', 'Closed'),
]

TEXT_DEFAULT = 'empty'


class TypeKey(models.Model):
    """type for key"""
    name = models.CharField(max_length=150, default=TEXT_DEFAULT)

    class Meta:
        verbose_name = 'TypeKey'
        verbose_name_plural = 'TypeKeys'

    def __str__(self):
        return self.name


class Key(models.Model):
    """Key for Note"""
    link = models.TextField(max_length=500, default=TEXT_DEFAULT)
    type_key = models.ForeignKey(TypeKey, on_delete=models.CASCADE, blank=True, related_name='type_key')

    class Meta:
        verbose_name = 'Key'
        verbose_name_plural = 'Keys'

    def __str__(self):
        return f'{self.link} / {self.type_key}'


class Owner(models.Model):
    """Owner for Note"""
    name = models.CharField(max_length=150, default=TEXT_DEFAULT)
    comment = models.TextField(max_length=500, default=TEXT_DEFAULT)

    class Meta:
        verbose_name = 'Owner'
        verbose_name_plural = 'Owners'

    def __str__(self):
        return self.name


class Source(models.Model):
    """Source for Note"""
    name = models.CharField(max_length=150, default=TEXT_DEFAULT)
    comment = models.TextField(max_length=500, default=TEXT_DEFAULT)

    class Meta:
        verbose_name = 'Source'
        verbose_name_plural = 'Sources'

    def __str__(self):
        return self.name


class Note(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, blank=True, related_name='note_owners')
    source = models.ForeignKey(Source, on_delete=models.CASCADE, blank=True, related_name='note_sources')
    key = models.ForeignKey(Key, on_delete=models.CASCADE, blank=True, related_name='note_keys')
    date_update = models.DateField(default=datetime.date.today)

    status = models.CharField(max_length=1, choices=STATUS, default=STATUS[0])
    text = models.TextField(default=TEXT_DEFAULT)
    comment = models.TextField(max_length=500, default=TEXT_DEFAULT)

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
        ordering = ['owner', 'source', 'date_update']

    def __str__(self):
        return f' for this owner - {self.owner} and sourse- {self.source} --- {self.text} - '
