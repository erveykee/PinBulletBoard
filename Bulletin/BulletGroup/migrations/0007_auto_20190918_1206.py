# Generated by Django 2.2.4 on 2019-09-18 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BulletGroup', '0006_media_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='content',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='posts',
            name='freeWrite',
            field=models.TextField(blank=True),
        ),
    ]
