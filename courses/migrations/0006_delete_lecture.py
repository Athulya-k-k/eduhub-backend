# Generated by Django 4.2.3 on 2023-07-19 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0002_alter_progress_lecture'),
        ('courses', '0005_remove_lecture_category_remove_lecture_course'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Lecture',
        ),
    ]