# Generated by Django 3.0.6 on 2020-06-24 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20200624_1445'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='account',
            new_name='username',
        ),
    ]