from django.db import models

STATUS_ACTIVE = [
    ('+', 'Active'),
    ('-', 'Closed'),
]

TEXT_DEFAULT = 'empty'


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
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, blank=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE, blank=True)
    date_update = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=1, choices=STATUS_ACTIVE, default=STATUS_ACTIVE[0])
    text = models.TextField(default=TEXT_DEFAULT)
    comment = models.TextField(max_length=500, default=TEXT_DEFAULT)

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
        ordering = ['owner', 'source', 'date_update']

    def __str__(self):
        return f'{self.source} - {self.text} - {self.owner}'
