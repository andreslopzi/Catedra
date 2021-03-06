# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-07 16:50
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateTimeField(default=datetime.datetime.now)),
                ('fin', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.IntegerField(default=0)),
                ('nombre', models.CharField(max_length=300)),
                ('monitores', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacion', models.CharField(max_length=20)),
                ('tipo_documento', models.CharField(choices=[('Cedula', 'Cedula'), ('Pasaporte', 'Pasaporte')], max_length=30)),
                ('nombre', models.CharField(max_length=200)),
                ('correo', models.CharField(max_length=100)),
                ('cursos', models.ManyToManyField(to='qr.Curso')),
            ],
        ),
        migrations.AddField(
            model_name='clase',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qr.Curso'),
        ),
        migrations.AddField(
            model_name='asistencia',
            name='clase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qr.Clase'),
        ),
        migrations.AddField(
            model_name='asistencia',
            name='estudiante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qr.Estudiante'),
        ),
        migrations.AddField(
            model_name='asistencia',
            name='monitor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
