from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from .serializers.serializer import VariableSerializer
from apps.sensors.models import Variable
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class MeasureListApi(ListAPIView):
    serializer_class = VariableSerializer
    
    def get_queryset(self):
        return Variable.objects.all()


class MeasureDetailApi(ListAPIView):
    serializer_class = VariableSerializer
        
    def get_queryset(self):
        sensor = self.kwargs['sen']     
        return Variable.objects.busqueda_sensor_last(sensor)  
    

class MeasureAddApi(CreateAPIView):
    serializer_class = VariableSerializer
    


