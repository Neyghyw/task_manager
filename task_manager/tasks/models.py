from django.contrib.auth.models import User
from django.db import models

from labels.models import Label
from statuses.models import Status


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=255,
                            unique=True,
                            verbose_name='Name')

    description = models.CharField(max_length=255,
                                   verbose_name='Description')

    status = models.ForeignKey(Status,
                               on_delete=models.PROTECT,
                               related_name='status',
                               verbose_name='Status')

    label = models.ManyToManyField(Label,
                                   related_name='labels',
                                   verbose_name='Label')

    creator = models.ForeignKey(User,
                                related_name='task_creator',
                                on_delete=models.PROTECT,
                                blank=False,
                                verbose_name='Creator')

    executor = models.ForeignKey(User,
                                 related_name='task_executor',
                                 on_delete=models.PROTECT,
                                 verbose_name='Executor')

    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
