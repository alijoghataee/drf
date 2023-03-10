# Generated by Django 4.1.5 on 2023-01-22 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('story_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='book_image/')),
                ('fav', models.BooleanField(default=False)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
