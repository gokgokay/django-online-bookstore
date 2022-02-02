# Generated by Django 3.2.6 on 2022-01-30 01:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('bio', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='profiles/%Y/%m/%d')),
                ('favorites', models.ManyToManyField(related_name='favorited_by', to='book.Book')),
                ('follows', models.ManyToManyField(related_name='followed_by', to='profile.Profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at', 'updated_at'],
                'abstract': False,
            },
        ),
    ]
