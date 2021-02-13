from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from core.serializers import UserSerializer, CreateUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Regresa la instancia de un usuario
    list:
        Regresa la lista de usuarios
    update:
        Actualiza un usuario
    partial_update:
        Actualiza un campo en particular de un usuario
    delete:
        Elimina un usuario
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes =[AllowAny]
        return[permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateUserSerializer
        return UserSerializer


