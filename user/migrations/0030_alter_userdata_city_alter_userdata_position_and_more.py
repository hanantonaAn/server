# Generated by Django 4.2.6 on 2024-05-04 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0029_userdata_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='city',
            field=models.TextField(default='Москва'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='position',
            field=models.TextField(default='Разработчик'),
        ),
        migrations.AlterField(
            model_name='userexperience',
            name='experience_years',
            field=models.CharField(default='between1And3'),
        ),
    ]
