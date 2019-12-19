from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from tags.models import Tags
from tags.serializers import TagsSerializers


class TagsViewSet(viewsets.ModelViewSet):
    """
       retrieve:
           Regresa un tag
       list:
           Regresa la lista de tags
       update:
           Actualiza un  tag
       partial_update:
           Actualiza un campo de un tag
       delete:
           elimina un tag
       """
    queryset = Tags.objects.all()
    serializer_class = TagsSerializers

    def get_permissions(self):
        if self.action in ['retrieve', 'list']:
            self.permission_classes = [AllowAny]
        return [permission() for permission in self.permission_classes]





