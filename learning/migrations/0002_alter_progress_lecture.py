# Generated by Django 4.2.3 on 2023-07-19 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('csession', '0001_initial'),
        ('learning', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progress',
            name='lecture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csession.lecture'),
        ),
    ]
