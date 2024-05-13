# Generated by Django 4.2.6 on 2024-05-13 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0031_alter_portfolio_portfolio_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='additional_info_show',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='city_show',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='contact_email_show',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='contact_telegram_show',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='curses_show',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='date_of_birth_show',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='education_level_show',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='font',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='font_color',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='font_size',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='fullname_show',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='graduation_date_show',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='graduation_place_show',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='languages_show',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='lastname_show',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='phone_number_show',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='position_show',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='sex_show',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='status_show',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='surname_show',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userexperience',
            name='font',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userexperience',
            name='font_color',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userexperience',
            name='font_size',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userexperience',
            name='show',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userskills',
            name='font',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userskills',
            name='font_color',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userskills',
            name='font_size',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userskills',
            name='show',
            field=models.BooleanField(default=True),
        ),
    ]