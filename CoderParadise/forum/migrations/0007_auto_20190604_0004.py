# Generated by Django 2.2.1 on 2019-06-03 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190531_0223'),
        ('forum', '0006_auto_20190604_0004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thumb',
            name='thumbUser',
        ),
        migrations.AddField(
            model_name='thumb',
            name='thumbUserProfile',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile'),
        ),
    ]