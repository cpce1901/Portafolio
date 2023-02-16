from rest_framework import serializers
from apps.sensors.models import Variable, Sensor, Equipo

class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'



class VariableSerializer(serializers.ModelSerializer):    

    class Meta:
        model = Variable
        get_latest_by = 'created'
        fields = (
           '__all__'
        ) 

    def to_representation(self, obj):
        print(obj)
        return {
            'id':obj.id,
            'sensor' : obj.sensor.id,   
            'created' : obj.created,         
            'me' : {
                'vln': {
                    'v1' : obj.v1,
                    'v2' : obj.v2,
                    'v3' : obj.v3,
                },
                'vll': {
                    'v13' : obj.v13,
                    'v23' : obj.v23,
                    'v12' : obj.v12,
                },
                'il': {
                    'i1' : obj.i1,
                    'i2' : obj.i2,
                    'i3' : obj.i3,
                },
                'pl': {
                    'p1' : obj.p1,
                    'p2' : obj.p2,
                    'p3' : obj.p3,
                },
                'ot': {
                    'pa' : obj.pa,
                    'fp' : obj.fp,
                    'hz' : obj.hz,
                },
            }
        }

   
   


