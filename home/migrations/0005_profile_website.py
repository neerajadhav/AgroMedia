# Generated by Django 3.2.8 on 2021-10-07 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]
