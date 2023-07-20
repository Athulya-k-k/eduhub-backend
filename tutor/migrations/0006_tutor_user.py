# Generated by Django 4.2.1 on 2023-06-26 05:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tutor', '0005_remove_tutor_experience_remove_tutor_is_admin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]