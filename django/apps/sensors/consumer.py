from .models import Variable, Sensor
from apps.api.serializers.serializer import VariableSerializer, SensorSerializer
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

import json
from asyncio import sleep



class MeasureConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        for i in range(1000):
            await self.send(json.dumps({'value': 'Conectado al websoket'}))
            await sleep(5)

    
        

    
