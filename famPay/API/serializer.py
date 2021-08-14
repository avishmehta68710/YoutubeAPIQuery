from rest_framework import serializers
from . import models


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = models.Video


class APIKeySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.APIKey
