# Generated by Django 3.0.5 on 2020-05-05 20:24

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='test',
            field=tinymce.models.HTMLField(default=''),
        ),
    ]