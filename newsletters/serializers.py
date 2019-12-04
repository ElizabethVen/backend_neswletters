from rest_framework import serializers

from newsletters.models import Newsletter


class NewsletterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Newsletter
        fields = ('name', 'description', 'image', 'target', 'frequency', 'created_at', 'updated_at', 'author',)