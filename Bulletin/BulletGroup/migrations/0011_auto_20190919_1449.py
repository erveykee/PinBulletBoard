# Generated by Django 2.2.4 on 2019-09-19 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BulletGroup', '0010_user_inuse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='inUse',
        ),
        migrations.AddField(
            model_name='codes',
            name='inUse',
            field=models.BooleanField(default=False),
        ),
    ]
