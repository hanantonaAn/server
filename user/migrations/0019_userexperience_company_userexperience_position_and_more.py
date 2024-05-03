# Generated by Django 4.2.6 on 2024-04-23 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_alter_userdata_curses_alter_userdata_languages'),
    ]

    operations = [
        migrations.AddField(
            model_name='userexperience',
            name='company',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userexperience',
            name='position',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='UserVacancy',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, default='NONE', null=True)),
                ('hh_id', models.CharField(blank=True, null=True)),
                ('name', models.CharField(blank=True, null=True)),
                ('area', models.CharField(blank=True, null=True)),
                ('salary_from', models.CharField(blank=True, null=True)),
                ('salary_to', models.CharField(blank=True, null=True)),
                ('address', models.CharField(blank=True, null=True)),
                ('url', models.CharField(blank=True, null=True)),
                ('company', models.CharField(blank=True, null=True)),
                ('requirements', models.CharField(blank=True, null=True)),
                ('responsobility', models.CharField(blank=True, null=True)),
                ('scedule', models.CharField(blank=True, null=True)),
                ('role', models.CharField(blank=True, null=True)),
                ('experience', models.CharField(blank=True, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]