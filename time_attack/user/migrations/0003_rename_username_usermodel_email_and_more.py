# Generated by Django 4.0.4 on 2022-05-27 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_usermodel_bio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='username',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='updated_at',
        ),
    ]
