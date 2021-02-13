from requests import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

from newsletters.models import Newsletter
from tags.models import Tags

from newsletters.serializers import NewsletterSerializer, CreateNewsletterSerializer
from tags.serializers import TagsSerializers


def page(args):
    pass


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


    def get_serializer_class(self):
        if self.action == 'create':
            return CreateNewsletterSerializer
        return NewsletterSerializer

