# Generated by Django 4.2.16 on 2024-09-26 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NameDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('person_name', models.CharField(max_length=255)),
                ('country_name', models.CharField(max_length=255)),
            ],
        ),
    ]
