from django.urls import path
from .views import AudioList, testView

app_name = 'streaming'
urlpatterns = [
    path('api/audios/', AudioList.as_view(), name="audio-list"),
    path('', testView, name="test"),
]