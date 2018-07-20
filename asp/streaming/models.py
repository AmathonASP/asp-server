from django.db import models

# ------------------------------------------------------------------
# TableName   : Audio
# Description : 음원 테이블
# ------------------------------------------------------------------
class Audio(models.Model):
    class Meta:
        verbose_name_plural = "음원 테이블"

    thumbnail = models.ImageField(upload_to="thumbnail/%Y/%m/%d", verbose_name="썸네일")
    artist = models.CharField(default=None, max_length=32, null=True, blank=True, verbose_name="아티스트")
    title = models.CharField(default=None, max_length=64, null=True, blank=True, verbose_name="타이틀")
