# Generated by Django 4.1.4 on 2023-05-01 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stogit', '0011_alter_stogitstats_losses_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stogitstats',
            name='total_points',
            field=models.IntegerField(default=0),
        ),
    ]