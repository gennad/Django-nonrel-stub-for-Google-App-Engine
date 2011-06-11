from django.db import models

LANG_CHOICES = (
    ('python', 'Python'),
    ('cpp', 'C++'),
)

class Snippet(models.Model):
    title = models.CharField(max_length=100)
    filename = models.CharField()
    code = models.CharField()
    lang = models.CharField(max_length=30, choices=LANG_CHOICES)

    def __unicode__(self):
        return self.name
