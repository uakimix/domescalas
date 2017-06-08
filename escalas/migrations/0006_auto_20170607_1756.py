# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-07 17:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escalas', '0005_bcis'),
    ]

    operations = [
        migrations.CreateModel(
            name='Duke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('item_01', models.PositiveSmallIntegerField(null=True)),
                ('item_02', models.PositiveSmallIntegerField(null=True)),
                ('item_03', models.PositiveSmallIntegerField(null=True)),
                ('item_04', models.PositiveSmallIntegerField(null=True)),
                ('item_05', models.PositiveSmallIntegerField(null=True)),
                ('item_06', models.PositiveSmallIntegerField(null=True)),
                ('item_07', models.PositiveSmallIntegerField(null=True)),
                ('item_08', models.PositiveSmallIntegerField(null=True)),
                ('item_09', models.PositiveSmallIntegerField(null=True)),
                ('item_10', models.PositiveSmallIntegerField(null=True)),
                ('item_11', models.PositiveSmallIntegerField(null=True)),
            ],
            options={
                'verbose_name': 'Duke',
                'verbose_name_plural': 'Escalas Duke',
            },
        ),
        migrations.CreateModel(
            name='Madrs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('item_01', models.PositiveSmallIntegerField(null=True)),
                ('item_02', models.PositiveSmallIntegerField(null=True)),
                ('item_03', models.PositiveSmallIntegerField(null=True)),
                ('item_04', models.PositiveSmallIntegerField(null=True)),
                ('item_05', models.PositiveSmallIntegerField(null=True)),
                ('item_06', models.PositiveSmallIntegerField(null=True)),
                ('item_07', models.PositiveSmallIntegerField(null=True)),
                ('item_08', models.PositiveSmallIntegerField(null=True)),
                ('item_09', models.PositiveSmallIntegerField(null=True)),
                ('item_10', models.PositiveSmallIntegerField(null=True)),
            ],
            options={
                'verbose_name': 'MADRS',
                'verbose_name_plural': 'Escalas MADRS',
            },
        ),
        migrations.AlterModelOptions(
            name='identificador',
            options={'verbose_name': 'Identificador', 'verbose_name_plural': 'Identificadores'},
        ),
        migrations.AddField(
            model_name='madrs',
            name='identificador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escalas.Identificador'),
        ),
        migrations.AddField(
            model_name='duke',
            name='identificador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escalas.Identificador'),
        ),
    ]