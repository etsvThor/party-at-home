from django.shortcuts import render
from django.conf import settings

# Create your views here.
# chat/views.py

def index(request):
    return render(request, 'chat/index.html')
def room(request, room_name):
    if settings.USE_HTTPS:
        ws_protocol = "wss"
    else:
        ws_protocol = "ws"

    return render(request,'chat/room.html', {
        'room_name': room_name,
        'ws_protocol': ws_protocol
        })
