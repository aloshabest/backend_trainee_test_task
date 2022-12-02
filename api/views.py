from django.shortcuts import render
from .models import Advert
from .serializers import AdvertSerializer
from rest_framework import viewsets


class AdvertViewSet(viewsets.ModelViewSet):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer

