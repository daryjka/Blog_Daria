# Generated by Django 3.0.4 on 2020-03-07 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=30)),
                ('tytul', models.CharField(max_length=100)),
                ('tresc', models.TextField()),
                ('data_publikacji', models.DateTimeField()),
            ],
        ),
    ]