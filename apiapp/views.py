from django.shortcuts import render
from .models import Singer, Song
from .serializers import SingerSerializer, SongSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class SingerListView(ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    
class SongListView(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    
    