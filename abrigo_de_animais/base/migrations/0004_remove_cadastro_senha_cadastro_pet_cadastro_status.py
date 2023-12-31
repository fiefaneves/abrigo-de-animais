# Generated by Django 4.2.6 on 2023-10-26 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adocoes', '0004_alter_adocoes_foto'),
        ('base', '0003_alter_cadastro_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadastro',
            name='senha',
        ),
        migrations.AddField(
            model_name='cadastro',
            name='pet',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='adocoes.adocoes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cadastro',
            name='status',
            field=models.BooleanField(default=None, null=True),
        ),
    ]
