# Generated by Django 3.2.4 on 2021-06-20 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20210620_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='view_count',
        ),
    ]
