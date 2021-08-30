# Generated by Django 3.2.6 on 2021-08-30 18:20

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=250)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='books/%Y/%m/%d')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField(default=10)),
                ('available', models.BooleanField(default=True)),
                ('description', models.TextField()),
                ('language', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('authors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='book.author')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='book.category')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
