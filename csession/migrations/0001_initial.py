# Generated by Django 4.2.3 on 2023-07-19 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0005_remove_lecture_category_remove_lecture_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sessions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=800)),
                ('description', models.CharField(max_length=800)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=600)),
                ('description', models.CharField(max_length=600)),
                ('type', models.CharField(max_length=100)),
                ('material', models.FileField(null=True, upload_to='photos/course')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csession.sessions')),
            ],
        ),
    ]