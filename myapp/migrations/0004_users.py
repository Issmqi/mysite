# Generated by Django 3.0.6 on 2020-06-03 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('create_time', models.DateField(auto_now=True)),
            ],
        ),
    ]