# Generated by Django 4.1.4 on 2023-04-27 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stogit', '0004_stogitstatus_point_stogitround'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stogitstatus',
            name='point',
            field=models.CharField(default='0', max_length=3),
        ),
    ]