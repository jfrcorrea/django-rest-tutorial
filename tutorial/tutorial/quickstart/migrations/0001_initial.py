# Generated by Django 3.2.7 on 2021-09-14 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChuckNorrisJoke',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('value', models.CharField(max_length=500)),
            ],
        ),
    ]
