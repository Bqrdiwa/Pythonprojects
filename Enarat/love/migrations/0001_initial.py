# Generated by Django 4.2 on 2023-05-15 00:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=16, unique=True)),
                ('password', models.CharField(max_length=16)),
                ('date_created', models.TimeField(default=django.utils.timezone.now)),
                ('ip', models.CharField(default='', max_length=128)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='love_user_set', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='love_user_set', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=12)),
                ('date_created', models.TimeField(default=django.utils.timezone.now)),
                ('thumbnail', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=12)),
                ('date_created', models.TimeField(default=django.utils.timezone.now)),
                ('file', models.FileField(upload_to='Albums-items/')),
                ('AlbumRelated', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='love.gallery')),
            ],
        ),
        migrations.CreateModel(
            name='ItemMSG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=64)),
                ('date_created', models.TimeField(default=django.utils.timezone.now)),
                ('galleryRelated', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='love.gallery')),
                ('itemRelated', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='love.item')),
                ('userRelated', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItemLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemRelated', models.ManyToManyField(to='love.item')),
                ('userRelated', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
