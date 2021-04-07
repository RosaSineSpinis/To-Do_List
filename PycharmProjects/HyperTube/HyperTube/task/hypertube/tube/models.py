from django.db import models

# Create your models here.
from django.urls import reverse
# from django.settings import MEDIA_ROOT, MEDIA_URL

from django.conf import settings


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Video(models.Model):
    file = models.FileField(upload_to=settings.MEDIA_ROOT+'/'+settings.MEDIA_URL)
    # file = models.FileField(upload_to=r'C:\Users\piotr\PycharmProjects\HyperTube\HyperTube\task\hypertube\media')
    title = models.CharField(max_length=255)

    # def get_absolute_url(self):
    #     '''grab url and make in consistent django - template so we do not need to care'''
    #     return reverse("video_filtering")

    def get_absolute_url(self):
        '''grab url and make in consistent django - template so we do not need to care'''
        return reverse("video_detail", kwargs={"my_id": self.id}) #f"/products/{self.id}/"


class VideoTag(models.Model):
    tag =        models.ForeignKey(Tag, on_delete=models.CASCADE,  related_name='tag')
    video =      models.ForeignKey(Video, on_delete=models.CASCADE,  related_name='video')

