# Generated by Django 4.1.4 on 2023-05-24 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('love', '0010_alter_gallery_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='ip',
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=256),
        ),
    ]