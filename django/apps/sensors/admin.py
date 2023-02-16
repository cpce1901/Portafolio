from django.contrib import admin
from .models import Equipo, Sensor, Variable

# Register your models here.
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'model')


class SensorAdmin(admin.ModelAdmin):
    list_display = ('name', 'equipo', 'locate')

    


class VariableAdmin(admin.ModelAdmin):
    list_display = ('created', 'sensor',
     'v1', 'v2', 'v3',
     'v13', 'v23', 'v12',
     'i1', 'i2', 'i3',
     'p1', 'p2', 'p3',
     'pa', 'fp', 'hz')
    ordering = ('-created',)

    list_filter = ('sensor__name',)


    


admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Sensor, SensorAdmin)
admin.site.register(Variable, VariableAdmin)
