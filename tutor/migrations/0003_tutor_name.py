# Generated by Django 4.2.1 on 2023-06-19 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0002_tutor_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='name',
            field=models.CharField(default='Default Name', max_length=50),
        ),
    ]
