from rest_framework import serializers

from tags.models import Tags


class TagsSerializers(serializers.ModelSerializer):

    class Meta:

        model = Tags
        fields = ('name', 'slug', 'created_at', 'updated_at', )