from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=255,
                            unique=True,
                            verbose_name=_('Name'))

    description = models.CharField(max_length=255,
                                   verbose_name=_('Description'))

    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created at'))

    def __str__(self):
        return self.name
