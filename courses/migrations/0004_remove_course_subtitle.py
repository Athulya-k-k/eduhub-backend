# Generated by Django 4.2.3 on 2023-07-17 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_remove_course_tutor_remove_course_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='subtitle',
        ),
    ]