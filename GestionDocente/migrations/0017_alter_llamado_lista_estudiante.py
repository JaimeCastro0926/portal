# Generated by Django 4.1.4 on 2023-01-18 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GestionDocente', '0016_llamado_lista_recurrente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='llamado_lista',
            name='Estudiante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='GestionDocente.estudiante'),
        ),
    ]
