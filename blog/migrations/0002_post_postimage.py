# Generated by Django 3.1.6 on 2021-03-03 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='postimage',
            field=models.ImageField(blank=True, upload_to='blog/media/postimages'),
        ),
    ]
