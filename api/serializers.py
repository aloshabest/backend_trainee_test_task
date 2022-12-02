from rest_framework.serializers import ModelSerializer
from .models import Advert


class AdvertSerializer(ModelSerializer):
    class Meta:
        model = Advert
        fields = '__all__'