from rest_framework import serializers

import newsletters
from newsletters.models import Newsletter


class NewsletterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Newsletter
        fields = ('name', 'description', 'image', 'target', 'frequency', 'created_at', 'updated_at', 'author', 'tags', )


class CreateNewsletterSerializer(serializers.ModelSerializer):
    """
    Create Newsletter Serializer
    """

    class Meta:
        model = Newsletter
        fields = ('name', 'description', 'image', 'target', 'frequency', 'created_at', 'updated_at', 'author', 'tags',)
