from django.db import models
from apps.api.manager import ApiManager

# Create your models here.
class Equipo(models.Model):
    marca = models.CharField('Marca', max_length=15)
    model = models.CharField('Modelo', max_length=20)
    image = models.ImageField('Imagen', upload_to='sensors')

    def __str__(self):
        return f'{self.marca}'

    
    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        

class Sensor(models.Model):
    name = models.CharField('Nombre', max_length=10, default='Sensor N', unique=True)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, verbose_name='Equipo', related_name='equipo')
    locate = models.CharField('Instalado en', max_length=20)

    def __str__(self):
        return f'{self.name}'

    
    class Meta:
        verbose_name = 'Sensor'
        verbose_name_plural = 'Sensores'
    

class Variable(models.Model):    
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, verbose_name='sensor', related_name='sensor')
    v1 = models.FloatField('Voltaje L1 - N')
    v2 = models.FloatField('Voltaje L2 - N')
    v3 = models.FloatField('Voltaje L3 - N')

    v13 = models.FloatField('Voltaje L1 - L3')
    v23 = models.FloatField('Voltaje L2 - L3')
    v12 = models.FloatField('Voltaje L1 - L2')

    i1 = models.FloatField('Corriente L1')
    i2 = models.FloatField('Corriente L2')
    i3 = models.FloatField('Corriente L3')

    p1 = models.FloatField('Potencia L1')
    p2 = models.FloatField('Potencia L2')
    p3 = models.FloatField('Potencia L3')

    pa = models.FloatField('Potencia Activa')
    fp = models.FloatField('Factor de potencia')
    hz = models.FloatField('Frecuencia')

    created = models.DateTimeField('Ingresado', auto_now=True)


    def __str__(self):
        return f'{self.sensor}'

    
    class Meta:
        verbose_name = 'Medida'
        verbose_name_plural = 'Medidas'


    objects = ApiManager()

