from django.contrib import admin
from .models import Audio

# ------------------------------------------------------------------
# TableName   : Audio
# Description : 음원 테이블
# ------------------------------------------------------------------
@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Audio._meta.fields]
