# Generated by Django 2.2 on 2019-05-30 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190530_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, default=None, upload_to='avatar'),
        ),
    ]
