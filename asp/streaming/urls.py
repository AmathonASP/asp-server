from django.urls import path
from .views import audio_list

app_name = 'streaming'
urlpatterns = [
    path('api/audios/', audio_list, name="audio-list"),
]