# Generated by Django 2.2.1 on 2019-06-08 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_student_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]
