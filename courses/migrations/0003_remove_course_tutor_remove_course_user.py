# Generated by Django 4.2.3 on 2023-07-17 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_tutor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='tutor',
        ),
        migrations.RemoveField(
            model_name='course',
            name='user',
        ),
    ]
