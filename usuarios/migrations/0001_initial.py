# Generated by Django 5.1.6 on 2025-02-15 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idProducto', models.IntegerField()),
                ('descripcion', models.CharField(max_length=80)),
                ('stock', models.IntegerField()),
                ('ubicacion', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'PRODUCTOS',
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idUsuario', models.IntegerField()),
                ('usuario', models.CharField(max_length=80)),
                ('contraseña', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=80)),
                ('apellido', models.CharField(max_length=80)),
            ],
            options={
                'db_table': 'USUARIOS',
            },
        ),
    ]
