from .models import Audio
from django.shortcuts import render
from rest_framework import generics
from .serializers import AudioSerializers

# Create your views here.

# 음원 리스트  및 생성 뷰
def testView(request):
    return render(request, 'test.html', {})

class AudioList(generics.ListCreateAPIView):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializers