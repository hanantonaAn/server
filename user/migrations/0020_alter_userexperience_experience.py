# Generated by Django 4.2.6 on 2024-04-23 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_userexperience_company_userexperience_position_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userexperience',
            name='experience',
            field=models.CharField(blank=True, null=True),
        ),
    ]
