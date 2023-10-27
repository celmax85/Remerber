from Api.models import User, Fichier, Categorie
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, FichierSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer

class FichierViewSet(viewsets.ModelViewSet):
    queryset = Fichier.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FichierSerializer