from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from login import consumer

websocket_urlPattern = [
    path('ws/user/',consumer.ChatConsumer),
]

application = ProtocolTypeRouter({
        'websocket' : AuthMiddlewareStack(URLRouter(websocket_urlPattern))
    }
)

    