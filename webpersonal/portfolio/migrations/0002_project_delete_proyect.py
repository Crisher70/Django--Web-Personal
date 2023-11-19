# Generated by Django 4.2.4 on 2023-11-19 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titulo')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
                ('image', models.ImageField(upload_to='projects', verbose_name='Imagen')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado en')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Actualizado en')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'proyectos',
                'ordering': ['-created_at'],
            },
        ),
        migrations.DeleteModel(
            name='Proyect',
        ),
    ]