# Generated by Django 3.2.4 on 2021-06-20 00:00

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20210619_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default='some content we have here', verbose_name='Content'),
            preserve_default=False,
        ),
    ]
