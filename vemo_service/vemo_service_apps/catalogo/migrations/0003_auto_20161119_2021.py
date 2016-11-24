# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 01:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Motor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('serie', models.CharField(blank=True, max_length=60, null=True)),
                ('tipoMotor', models.CharField(blank=True, max_length=60, null=True)),
                ('marca', models.CharField(blank=True, max_length=60, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'verbose_name_plural': 'Motores',
                'verbose_name': 'Motor',
            },
        ),
        migrations.AlterModelOptions(
            name='cliente',
            options={'permissions': (('list_cliente', 'Can list cliente'), ('get_cliente', 'Can get cliente')), 'verbose_name': 'cliente', 'verbose_name_plural': 'clientes'},
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='codigo',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='estado',
        ),
        migrations.AddField(
            model_name='cliente',
            name='apellidoM',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='apellidoP',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='cell',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='fecha',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='tipoVenta',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='motor',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Cliente'),
        ),
    ]