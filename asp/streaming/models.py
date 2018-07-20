from django.db import models
from mutagen.mp3 import MP3
from django.db.models.signals import post_save, pre_save

# ------------------------------------------------------------------
# TableName   : Audio
# Description : 음원 테이블
# ------------------------------------------------------------------
class Audio(models.Model):
    class Meta:
        verbose_name_plural = "음원 테이블"
    BITRATE = (
        ('320', 'High'),
        ('196', 'Mid'),
        ('128', 'Low')
    )
    thumbnail = models.ImageField(upload_to="thumbnail/%Y/%m/%d", verbose_name="썸네일")
    artist = models.CharField(default=None, max_length=32, null=True, blank=True, verbose_name="아티스트")
    title = models.CharField(default=None, max_length=64, null=True, blank=True, verbose_name="타이틀")
    max_bitrate = models.CharField(max_length=10, choices=BITRATE, default='Low', verbose_name="최대품질")
    audio = models.FileField(upload_to="audio/%Y/%m/%d", verbose_name="음원")

#  BitRate 저장
def audio_pre_save(sender, instance, *args, **kwargs):
    audio = MP3(instance.audio)
    bitrate = audio.info.bitrate

    if (bitrate >= 320000):
        bitrate="320"
    elif ( 320000 < bitrate <= 196000):
        bitrate = "196"
    else:
        bitrate = "128"

    instance.max_bitrate = bitrate

#  분할 저장
from django.conf import settings
import subprocess
import sys
import os
def audio_post_save(sender, instance, *args, **kwargs):
    filename, ext = os.path.splitext(str(instance.audio))
    ROOT = settings.MEDIA_ROOT.replace('\\', '/')+"/"

    try:
        if not (os.path.isdir(ROOT+str(instance.id))):
            os.makedirs(os.path.join(ROOT+str(instance.id)))
    except:
        pass


    def Export(kpbs):
        ext = "ffmpeg -i " + ROOT + str(instance.audio) + \
              " -acodec mp3 -ar 44100 -ab "+str(kpbs)+"k -f segment -segment_time 20 " \
              "-segment_list_size 0 -segment_list_flags -cache " \
              "-segment_format mp3 -segment_list " \
              + ROOT + str(instance.id) + "/" + filename+".m3u8 " \
              + ROOT + str(instance.id) + "/" + filename+"%d.mp3"

        # subprocess.call(ext, shell=True)
        # subprocess.check_output(ext, shell=True)
        theproc = subprocess.Popen([sys.executable, ext])
        theproc.communicate()

pre_save.connect(audio_pre_save, sender=Audio)
post_save.connect(audio_post_save, sender=Audio)