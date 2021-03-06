# Generated by Django 3.2.8 on 2021-10-26 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_cliente_observacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='observacao',
            field=models.TextField(max_length=200),
        ),
    ]
