# Generated by Django 4.2.3 on 2023-07-19 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_remove_course_subtitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='Category',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='course',
        ),
    ]
