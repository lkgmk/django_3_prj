# Generated by Django 4.2.16 on 2024-10-08 06:33

import crud_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0004_author_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='reg_no',
            field=models.IntegerField(validators=[crud_app.models.check_reg_no]),
        ),
    ]
