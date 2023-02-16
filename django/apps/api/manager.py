from django.db import models

class ApiManager(models.Manager):

    # Busqueda de sensor en modelo sensor para entregar en panatalla sus medidas
    def busqueda_sensor(self, sensor):   
            return self.filter(sensor = sensor).order_by('-created')
        
    
    # Busqueda de sensor en modelo sensor para entregar en panatalla ultimo dato de medidas
    def busqueda_sensor_last(self, sensor):   
            return self.filter(sensor = sensor).order_by('-created')[:1]