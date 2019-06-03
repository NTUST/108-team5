# Generated by Django 2.2.1 on 2019-06-03 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190531_0223'),
        ('forum', '0004_auto_20190603_2235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='postUser',
        ),
        migrations.AddField(
            model_name='comment',
            name='postUserProfile',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile'),
        ),
    ]
