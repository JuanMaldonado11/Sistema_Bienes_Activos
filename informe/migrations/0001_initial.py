# Generated by Django 3.1.6 on 2021-02-11 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('activos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Informe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipobienactivo', models.CharField(default='N/A', max_length=30)),
                ('codigo_acta', models.CharField(default='N/A', max_length=10)),
                ('informe', models.TextField()),
                ('fecha', models.DateField()),
                ('activo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activos.activo')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='director_informe', to=settings.AUTH_USER_MODEL)),
                ('revisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revisor_informe', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Informe',
                'verbose_name_plural': 'Informes',
            },
        ),
    ]