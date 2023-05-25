from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
# Create your models here.

POSITION_CHOICES = [
    ('PORTERO', 'Portero'),
    ('DEFENZA', (
        ('CENTRAL', 'Central'),
        ('LATERAL', 'Lateral'),
        ('LIBRE', 'Libre'),
        ('CARRILERO', 'Carrilero'),
    )),
    ('CENTRO CAMPISTA', (
        ('PIVOTE', 'Pivote'),
        ('MEDIA PUNTA', 'Media Punta'),
        ('VOLANTE', 'Volante'),
        ('INTERIOR', 'Interior'),
    )),
    ('DELANTERO', (
        ('SEGUNDO DEL', 'Segundo Del'),
        ('CENTRO', 'Centro'),
        ('EXTREMO DEL', 'Extremo Del'),
    )),
]


CAMISAS_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
    ("11", "11"),
    ("12", "12"),
    ("13", "13"),
    ("14", "14"),
    ("15", "15"),
    ("16", "16"),
    ("17", "17"),
    ("18", "18"),
    ("19", "19"),
    ("20", "20"),
    ("21", "21"),
    
)

ESTADO_CHOICES = [
    ('PENDIENTE', 'Pendiente'),
    ('PROGRAMADO', 'Programado'),
    ('FINALIZADO', 'Finalizado'),
]
class Estadios(models.Model):
    name = models.CharField(max_length=230)
    img = models.ImageField(default=None, upload_to='media/')
    
    def __str__(self) :
        return self.name
    

class Ligas(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(default=None, upload_to='media/')
  
    def __str__(self) :
        return self.name

class Coach(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(default=None, upload_to='media/')
     
    def __str__(self) :
        return self.name
    
    
class Arbitros(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(default=None, upload_to='media/')
     
    def __str__(self) :
        return self.name
    


class Equipos(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(default=None, upload_to='media/')  
    ligas = models.ForeignKey(Ligas, on_delete=models.PROTECT, related_name='equipos', default=None)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, null=True)  # Permitir valores nulos
    
    
    
    def __str__(self) :
        return self.name
    
class Jugadores(models.Model):
    name = models.CharField(max_length=200)
    numeroCamisa = models.CharField(max_length=30, choices=CAMISAS_CHOICES, default='1')
    posicion = models.CharField(max_length=20, choices=POSITION_CHOICES, default='PORTERO')
    equipo = models.ForeignKey(Equipos, on_delete=models.CASCADE, related_name='jugadores')
    img = models.ImageField(default=None, upload_to='media/')

    def __str__(self):
        return self.name


class Partidos(models.Model):
    equipo1 = models.ForeignKey(Equipos, on_delete=models.CASCADE, related_name='partidos_equipo1')
    equipo2 = models.ForeignKey(Equipos, on_delete=models.CASCADE, related_name='partidos_equipo2')
    liga = models.ForeignKey(Ligas, on_delete=models.CASCADE)
    estadio = models.ForeignKey(Estadios, on_delete=models.CASCADE)
    arbitro = models.ForeignKey(Arbitros, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='PENDIENTE')
    

    def get_titulo_partido(self):
        return f"{self.equipo1.name} vs {self.equipo2.name}"

    def get_estado_display(self):
        return dict(ESTADO_CHOICES).get(self.estado, 'Desconocido')
    
    def clean(self):
        if self.equipo1.ligas != self.equipo2.ligas:
            raise ValidationError("Los equipos no pertenecen a la misma liga. Verifica la lista a la liga que pertenecen los equipos")
        
        if self.equipo1 == self.equipo2:
            raise ValidationError("No se puede programar un partido entre el mismo equipo.")
        
        if Partidos.objects.filter(fecha=self.fecha).exists():
            raise ValidationError("La fecha y hora seleccionadas ya están ocupadas por otro partido.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)