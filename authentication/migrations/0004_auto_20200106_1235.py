# Generated by Django 3.0.2 on 2020-01-06 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20200106_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpmodel',
            name='otp',
            field=models.IntegerField(),
        ),
    ]