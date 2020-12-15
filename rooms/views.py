from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Room
from .serializers import RoomSerializer


class ListRoomsView(APIView):
    def get(self, request):
        rooms = Room.objects.all()
        serialized_rooms = RoomSerializer(rooms, many=True)
        return Response(data=serialized_rooms.data)