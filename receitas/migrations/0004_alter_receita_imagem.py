# Generated by Django 5.1.1 on 2024-12-28 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0003_alter_receita_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='fotos'),
        ),
    ]