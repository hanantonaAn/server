# Generated by Django 4.2.6 on 2024-05-04 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0028_userdata_border_radius_userdata_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='position',
            field=models.TextField(blank=True, null=True),
        ),
    ]
