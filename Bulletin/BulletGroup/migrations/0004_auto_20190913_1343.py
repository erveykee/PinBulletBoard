# Generated by Django 2.2.4 on 2019-09-13 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BulletGroup', '0003_auto_20190913_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='codes',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='BulletGroup.Codes'),
        ),
    ]