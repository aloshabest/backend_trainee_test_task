from rest_framework import serializers
from .models import Advert


def title_valid(title):
    if len(title) > 200:
        raise serializers.ValidationError('description should be no more than 1000 letters')
    return title


def desc_valid(desc):
    if len(desc) > 1000:
        raise serializers.ValidationError('description should be no more than 1000 letters')
    return desc


def images_valid(images):
    if len(images) > 3:
        raise serializers.ValidationError('should be no more than 3 photos')
    return images


class AdvertSerializer(serializers.ModelSerializer):
    title = serializers.CharField(validators=[title_valid])
    description = serializers.CharField(validators=[desc_valid], required=False)
    images = serializers.JSONField(validators=[images_valid], required=False)

    def __init__(self, *args, **kwargs):
        super(AdvertSerializer, self).__init__(*args, **kwargs)
        if self.context['request'].method in ('GET', ):
            fields = self.context['request'].query_params.get('fields')
            if fields:
                fields = fields.split(',') + ['title', 'photo', 'price']
            else:
                fields = ['title', 'photo', 'price']
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.images:
            representation['photo'] = instance.images[0] if len(instance.images) > 0 else None
        return representation

    class Meta:
        model = Advert
        fields = '__all__'
