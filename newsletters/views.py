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

    @action(detail=True, methods=['GET'])
    def tags(self, request, pk=None):
        """
        Regresa los tags relacionados a un boletin
        """
        newsletter = self.paginate_queryset(tags)

        if page:  # if page is not None:
            serialized = TagsSerializers(page, many=True)
            return self.get_paginated_response(serialized.data)



