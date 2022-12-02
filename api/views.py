from rest_framework.response import Response
from .models import Advert
from .serializers import AdvertSerializer
from rest_framework import viewsets, filters


class ListViewSet(viewsets.ModelViewSet):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', ]
    ordering_fields = ['id', 'price', 'created_at', 'title']
    ordering = ['id']
