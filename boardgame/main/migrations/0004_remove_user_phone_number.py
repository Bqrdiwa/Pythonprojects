# Generated by Django 4.1.4 on 2023-04-16 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_profile_age_alter_profile_bio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
    ]