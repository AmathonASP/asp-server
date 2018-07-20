from .models import Audio
from rest_framework import status
from .serializers import AudioSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

# 음원 리스트  및 생성 뷰
# class AudioList(APIView):
#     """
#     List all Audio, or create a new Audio
#     """
#     def get(self, request, format=None):
#         audio = Audio.objects.all()
#         serializer = AudioSerializers(audio, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = AudioSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def removekey(d, key):
    r = dict(d)
    del r[key]
    return r

@api_view(['GET', 'POST'])
def audio_list(request):
    if request.method == 'GET':
        audio = Audio.objects.all()
        serializer = AudioSerializers(audio, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # 데이터 형식에 맞게 저장
        serializer = AudioSerializers(data=removekey(request.data, 'audio'))

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # 오디오 파일 분할 저장
        audio_file = request.data['audio']
        print(audio_file,"을 분할 저장합니다.")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)