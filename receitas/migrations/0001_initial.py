# Generated by Django 5.1.1 on 2024-12-12 01:10

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
                ('imagem', models.CharField(max_length=150)),
                ('autor', models.CharField(max_length=150)),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]