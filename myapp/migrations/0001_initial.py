# Generated by Django 3.0.6 on 2020-06-01 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16)),
                ('age', models.SmallIntegerField()),
                ('sex', models.CharField(max_length=1)),
                ('classid', models.CharField(max_length=8)),
            ],
            options={
                'db_table': 'stu',
            },
        ),
    ]
