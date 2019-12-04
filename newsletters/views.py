from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from newsletters.models import Newsletter
from newsletters.serializers import NewsletterSerializer


class NewsletterViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Regresa un boletin
    list:
        Regresa la listade boletines
    update:
        Actualiza un  boletin
    partial_update:
        Actualiza un campo de un boletin
    delete:
        elimina un boletin
    """
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer

    def get_permissions(self):
        if self.action in ['retrieve', 'list']:
            self.permission_classes = [AllowAny]
        return [permission() for permission in self.permission_classes]

