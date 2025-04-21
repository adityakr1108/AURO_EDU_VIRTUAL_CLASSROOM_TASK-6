import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from video_chat.routing import websocket_urlpatterns  # Import WebSocket URLs

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'virtual_classroom.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
