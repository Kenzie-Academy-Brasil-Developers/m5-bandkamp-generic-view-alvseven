from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView
from .serializers import SongSerializer

class SongView(ListCreateAPIView, PageNumberPagination):
    
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        return serializer.save(album_id=self.kwargs['pk'])
