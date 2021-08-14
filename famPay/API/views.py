from httplib2 import Response
from rest_framework import generics
from . import models
from django.core import paginator, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializer
from rest_framework.generics import ListAPIView


class index(ListAPIView):
    queryset = models.Video.objects.all().order_by('-publishing_date_time')
    serializer_class = serializer.VideoSerializer


@api_view(['GET'])
def search(req, title, description):
    try:
        result = models.Video.objects.all().filter(
            video_title__contains=title, description__contains=description)
        serialize = serializer.VideoSerializer(result, many=True)
    except:
        result = models.Video.objects.all().filter(
            video_title__contains=title.lower(), description__contains=description.lower())
        serialize = serializer.VideoSerializer(result, many=True)
    return Response(serialize.data)


class AddAPIKey(generics.CreateAPIView):

    serializer_class = serializer.APIKeySerializer
