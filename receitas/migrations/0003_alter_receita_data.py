# Generated by Django 5.1.1 on 2024-12-28 01:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0002_receita_publicada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='data',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]