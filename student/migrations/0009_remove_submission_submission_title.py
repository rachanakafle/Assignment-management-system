# Generated by Django 2.1.4 on 2019-01-12 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_auto_20190112_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='submission_title',
        ),
    ]
