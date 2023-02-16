from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Sensor, Variable, Equipo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, Http404, HttpResponseNotFound
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404


# Create your views here.
class ListSensor(LoginRequiredMixin, ListView):
    template_name = 'sensors/listsensor.html'
    model = Sensor
    context_object_name = 'sensors'
    login_url = reverse_lazy('users_app:login')


class ListMeasure(LoginRequiredMixin, ListView):
    template_name = 'sensors/listmeasure.html'
    model = Variable
    context_object_name = 'me'
    login_url = reverse_lazy('users_app:login') 

    def get_queryset(self):
        queryset = super(ListMeasure, self).get_queryset()
        sensor_b = self.kwargs['sen']    
        try:    
            lista = Variable.objects.filter(sensor_id = sensor_b).latest('created') 
        except Variable.DoesNotExist:
            lista = None
            
        return lista
        
            
        
        
        
        
   



   
    

    