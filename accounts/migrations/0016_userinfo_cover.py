# Generated by Django 3.1.6 on 2021-07-07 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20210621_0146'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='cover',
            field=models.ImageField(blank=True, default='media/defaultcover.png', upload_to='cover_photo'),
        ),
    ]
