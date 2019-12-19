from rest_framework import serializers

from newsletters.serializers import NewsletterSerializer
from tags.models import Tags


class TagsSerializers(serializers.ModelSerializer):

    """
    General purpose Tags serializer
    """
    tags = NewsletterSerializer(many=True, read_only=True)

    class Meta:

        model = Tags
        fields = ('tags', 'created_at', 'updated_at')


class CreateTagsSerializer(serializers.ModelSerializer):
    """
    Create Tags Serializer
    """

    class Meta:
        model = Tags
        fields = ('tags', 'created_at', 'updated_at')
