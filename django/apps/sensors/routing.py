from django.urls import path
from .consumer import MeasureConsumer

ws_urlpatterns = [
    path(r'ws/<sen>/', MeasureConsumer.as_asgi())
]