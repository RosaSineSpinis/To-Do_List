from django.contrib import admin

# Register your models here.
from .models import Tag, Video, VideoTag

admin.site.register(Tag)
admin.site.register(Video)
admin.site.register(VideoTag)
