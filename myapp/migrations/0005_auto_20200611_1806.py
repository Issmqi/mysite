# Generated by Django 3.0.6 on 2020-06-11 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_users'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='UserInfo',
        ),
    ]
