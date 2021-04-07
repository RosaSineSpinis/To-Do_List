from django.forms import ModelForm, Form

from tube.models import Video, Tag, VideoTag


class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = [
            'file',
            'title',
        ]


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = [
            'name',
        ]


class VideoTagForm(Form):
    pass
    # class Meta:
        # fields = "__all__"
        # exclude = ('VideoForm', 'TagForm')
