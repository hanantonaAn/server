# Generated by Django 4.2.6 on 2024-05-02 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_remove_userexperience_experience_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='uservacancy',
            name='time_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
