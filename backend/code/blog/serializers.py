from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    positive_number = serializers.IntegerField(min_value=0)

    class Meta:
        model = Post
        fields = ["id", "title", "body", "positive_number"]
