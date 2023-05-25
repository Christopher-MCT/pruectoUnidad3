# Generated by Django 4.2.1 on 2023-05-23 03:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arbitros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('img', models.ImageField(default=None, upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('img', models.ImageField(default=None, upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Equipos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('img', models.ImageField(default=None, upload_to='media/')),
                ('coach', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modelTeams.coach')),
            ],
        ),
        migrations.CreateModel(
            name='Estadios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=230)),
                ('img', models.ImageField(default=None, upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Ligas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('img', models.ImageField(default=None, upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Partidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('creado', models.BooleanField(default=False)),
                ('arbitro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelTeams.arbitros')),
                ('equipo1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partidos_equipo1', to='modelTeams.equipos')),
                ('equipo2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partidos_equipo2', to='modelTeams.equipos')),
                ('estadio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelTeams.estadios')),
                ('liga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelTeams.ligas')),
            ],
        ),
        migrations.CreateModel(
            name='Jugadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('numeroCamisa', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21')], default='1', max_length=30)),
                ('posicion', models.CharField(choices=[('PORTERO', 'Portero'), ('DEFENZA', (('CENTRAL', 'Central'), ('LATERAL', 'Lateral'), ('LIBRE', 'Libre'), ('CARRILERO', 'Carrilero'))), ('CENTRO CAMPISTA', (('PIVOTE', 'Pivote'), ('MEDIA PUNTA', 'Media Punta'), ('VOLANTE', 'Volante'), ('INTERIOR', 'Interior'))), ('DELANTERO', (('SEGUNDO DEL', 'Segundo Del'), ('CENTRO', 'Centro'), ('EXTREMO DEL', 'Extremo Del')))], default='PORTERO', max_length=20)),
                ('img', models.ImageField(default=None, upload_to='media/')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jugadores', to='modelTeams.equipos')),
            ],
        ),
        migrations.AddField(
            model_name='equipos',
            name='ligas',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='equipos', to='modelTeams.ligas'),
        ),
    ]
