# Generated by Django 3.2.4 on 2021-06-19 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'get_latest_by': ['-timestamp_created'], 'ordering': ['-timestamp_created']},
        ),
    ]
