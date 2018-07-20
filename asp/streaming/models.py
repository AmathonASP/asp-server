from django.conf import settings
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

def export(instance, kbps):

    input_path = settings.MEDIA_ROOT + str(instance.audio)
    print('kbps: ', kbps)
    if int(kbps) >= 320:
        bit_rate = '320k'

        output_path = "{media_root}{instance_id}/{bit_rate}/{output_name}".format(media_root=settings.MEDIA_ROOT, instance_id=instance.id, bit_rate=bit_rate, output_name=instance.title)

        dirpath = os.path.dirname(output_path)
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)

        ext = "ffmpeg -i {input_path} -acodec mp3 -ar 44100 -ab {bit_rate} -f segment -segment_time 20 -segment_list_size 0 -segment_list_flags -cache -segment_format mp3 -segment_list {output_path}.m3u8 {output_path}%d.mp3".format(input_path=input_path, output_path=output_path, bit_rate=bit_rate)
        subprocess.call(ext, shell=True)

    if int(kbps) >= 192:
        bit_rate = '192k'

        output_path = "{media_root}{instance_id}/{bit_rate}/{output_name}".format(media_root=settings.MEDIA_ROOT, instance_id=instance.id, bit_rate=bit_rate, output_name=instance.title)

        dirpath = os.path.dirname(output_path)
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)

        ext = "ffmpeg -i {input_path} -acodec mp3 -ar 44100 -ab {bit_rate} -f segment -segment_time 20 -segment_list_size 0 -segment_list_flags -cache -segment_format mp3 -segment_list {output_path}.m3u8 {output_path}%d.mp3".format(input_path=input_path, output_path=output_path, bit_rate=bit_rate)
        subprocess.call(ext, shell=True)


    if int(kbps) >= 128:
        bit_rate = '128k'

        output_path = "{media_root}{instance_id}/{bit_rate}/{output_name}".format(media_root=settings.MEDIA_ROOT, instance_id=instance.id, bit_rate=bit_rate, output_name=instance.title)

        dirpath = os.path.dirname(output_path)
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)

        ext = "ffmpeg -i {input_path} -acodec mp3 -ar 44100 -ab {bit_rate} -f segment -segment_time 20 -segment_list_size 0 -segment_list_flags -cache -segment_format mp3 -segment_list {output_path}.m3u8 {output_path}%d.mp3".format(input_path=input_path, output_path=output_path, bit_rate=bit_rate)
        subprocess.call(ext, shell=True)

def audio_post_save(sender, instance, *args, **kwargs):
    export(instance, instance.max_bitrate)


pre_save.connect(audio_pre_save, sender=Audio)
post_save.connect(audio_post_save, sender=Audio)
