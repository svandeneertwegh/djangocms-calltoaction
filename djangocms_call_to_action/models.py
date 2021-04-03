from django.db import models

from cms.models import CMSPlugin


class CallToAction(CMSPlugin):
    container = models.CharField(verbose_name='Container', choices=(('container', 'container'), ('container-fluid', 'container_fluid')), max_length=255)
    title = models.CharField(verbose_name='Titel', max_length=255)
    subtitle = models.CharField(verbose_name='Subtitel', max_length=255)
    # link = models.

    def __str__(self):
        return self.title
