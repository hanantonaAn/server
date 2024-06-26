# Generated by Django 4.2.6 on 2024-04-06 11:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_alter_portfolio_heading_ids_alter_portfolio_link_ids_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('hashtag', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sphere',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sphere', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='portfolio',
            name='hashtag_ids',
            field=models.ManyToManyField(blank=True, null=True, related_name='porfolio_hashtags', to='user.hashtag'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='sphere_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.sphere'),
        ),
    ]
