# Generated by Django 4.1.4 on 2023-04-28 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Stogit', '0005_alter_stogitstatus_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stogitround',
            name='cardOwner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Stogit.stogitplayer'),
        ),
    ]
