# Generated by Django 4.2.6 on 2023-10-26 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adocoes', '0003_rename_historico_de_saúde_adocoes_historico_de_saude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adocoes',
            name='foto',
            field=models.ImageField(blank=True, default='fotos_pets/', null=True, upload_to='fotos_pets'),
        ),
    ]
