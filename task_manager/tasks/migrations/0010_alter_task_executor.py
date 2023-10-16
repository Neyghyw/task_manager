# Generated by Django 3.2.21 on 2023-10-16 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0009_alter_task_executor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='executor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='task_executor', to=settings.AUTH_USER_MODEL, verbose_name='Executor'),
        ),
    ]
