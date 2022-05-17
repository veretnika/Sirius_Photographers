from .models import Rest
from rest_framework import viewsets, permissions
from .serializers import RestSerializer

class RestViewSet(viewsets.ModelViewSet):
    queryset = Rest.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = RestSerializer
    