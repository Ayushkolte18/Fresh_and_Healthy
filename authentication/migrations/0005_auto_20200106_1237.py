# Generated by Django 3.0.2 on 2020-01-06 12:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20200106_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdevice',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
