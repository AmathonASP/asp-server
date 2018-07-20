from rest_framework import serializers
from .models import Audio

class AudioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = [
            'id',
            'thumbnail',
            'artist',
            'title',
        ]