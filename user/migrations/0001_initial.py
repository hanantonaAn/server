# Generated by Django 4.2.6 on 2024-04-04 13:32

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('password', models.TextField(max_length=30)),
                ('username', models.TextField(max_length=30, unique=True)),
                ('email', models.TextField(unique=True)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserSkills',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('skills', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), null=True, size=None)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserExperience',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('experience', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), null=True, size=None)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.TextField(null=True)),
                ('additional_info', models.TextField(null=True)),
                ('fullname', models.TextField(null=True)),
                ('surname', models.TextField(null=True)),
                ('lastname', models.TextField(null=True)),
                ('phone_number', models.TextField(null=True, unique=True)),
                ('contact_telegram', models.TextField(null=True, unique=True)),
                ('contact_email', models.TextField(null=True, unique=True)),
                ('city', models.TextField(null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('sex', models.TextField(null=True)),
                ('graduation_place', models.TextField(null=True)),
                ('graduation_date', models.DateField(null=True)),
                ('languages', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20), null=True, size=None)),
                ('curses', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), null=True, size=None)),
                ('picture', models.ImageField(null=True, upload_to='profile_photo/')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
