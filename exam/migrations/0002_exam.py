# Generated by Django 5.0.2 on 2024-02-22 20:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0002_rename_caeer_career'),
        ('exam', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=0.0, verbose_name='Calificaxión')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career.career', verbose_name='Carrera')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.stage', verbose_name='Etapa')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'examen',
                'verbose_name_plural': 'examenes',
            },
        ),
    ]
