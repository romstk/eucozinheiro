# Generated by Django 5.1.1 on 2025-03-09 13:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('ingredientes', models.TextField()),
                ('preparo', models.TextField()),
                ('imagem', models.ImageField(blank=True, upload_to='fotos')),
                ('data', models.DateTimeField(default=datetime.datetime.now)),
                ('publicada', models.BooleanField(default=False)),
            ],
        ),
    ]
