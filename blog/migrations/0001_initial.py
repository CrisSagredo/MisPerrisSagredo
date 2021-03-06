# Generated by Django 2.1.2 on 2018-10-23 14:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postulante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.CharField(max_length=200)),
                ('rut', models.CharField(max_length=200)),
                ('nombre', models.TextField()),
                ('fechaNacimiento', models.DateTimeField(default=django.utils.timezone.now)),
                ('telefono', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=200)),
                ('comuna', models.CharField(max_length=200)),
                ('tipoVivienda', models.CharField(max_length=200)),
                ('fechaPostulacion', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
