from rest_framework import serializers

from newsletters.serializers import NewsletterSerializer
from tags.models import Tags


class TagsSerializers(serializers.ModelSerializer):

    """
    General purpose Tags serializer
    """
    #name = NewsletterSerializer(many=True, read_only=True)

    class Meta:

        model = Tags
        fields = ('name', 'created_at', 'updated_at')


class CreateTagsSerializer(serializers.ModelSerializer):
    """
    Create Tags Serializer
    """

    class Meta:
        model = Tags
        fields = ('name', 'created_at', 'updated_at')
