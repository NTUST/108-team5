# Generated by Django 2.2.1 on 2019-06-03 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_auto_20190604_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='postUserProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile'),
        ),
    ]
