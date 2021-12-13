# Generated by Django 4.0 on 2021-12-12 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('ListId', models.AutoField(primary_key=True, serialize=False)),
                ('ListName', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('TaskId', models.AutoField(primary_key=True, serialize=False)),
                ('TaskName', models.CharField(max_length=500)),
                ('List', models.CharField(max_length=500)),
                ('Deadline', models.DateField()),
                ('Status', models.BooleanField(null=True)),
            ],
        ),
    ]
