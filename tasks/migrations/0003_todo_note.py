# Generated by Django 3.0.3 on 2020-04-27 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20200427_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='note',
            field=models.TextField(blank=True),
        ),
    ]
