from django.shortcuts import render, get_object_or_404, reverse, HttpResponseRedirect,\
    resolve_url, redirect
from django.http import HttpResponse

from .models import Video, Tag, VideoTag
# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.views import View

from django.contrib.auth.views import LoginView, LogoutView

from django.conf import settings
from django.urls import reverse_lazy
from .forms import VideoForm, TagForm
    # VideoTagForm
from django.template.context_processors import csrf
import os


def video_raw_view(request, my_str):
    print("my_str", my_str)
    video_file = ""
    print("os.path.join(settings.MEDIA_ROOT, my_str", os.path.join(settings.MEDIA_ROOT, my_str))
    with open(os.path.join(settings.MEDIA_ROOT, my_str), 'rb') as vide:
        video_file = vide.read()
    response = HttpResponse(video_file, content_type="video/mp4")
    response["Accept-Ranges"] = "bytes"
    return response


def video_detail_view(request, my_id):

    if request.method == 'GET':
        # print(request.GET)
        word = request.GET.get('tag')
        if word:
            vid = VideoTag.objects.all().filter(tag__name=word)
            # print("vid", vid)
            # print("vid.first().video", vid.first().video.title)
            queryset = Video.objects.all().filter(title=vid.first().video.title)
            context = {
                "object_list": queryset,
                "videos_number": queryset.count()
            }
            return render(request, "home.html", context)
        else:
            print("else is working")
            obj = get_object_or_404(Video, id=my_id)
            print("bj.title ", obj.title)
            print("obj", obj)
            video_tags = VideoTag.objects.filter(video=obj)
            print("video_tags", video_tags)
            tags = []
            for tag in video_tags:
                tags.append(tag.tag)
            # vid_tag = VideoTag.objects.all().get()

            context = {
                'title': obj.title,
                'tags': tags,
                'url': os.path.join(settings.MEDIA_URL + str(obj.file))
            }
            # print("tags", context['tags'].first().name)
            # print("context['url'], ", context['url'])

    return render(request, "video_detail.html", context)


# def tag_filter_video(request, my_str):
#
#     if request.method == 'GET':
#         print(request.GET)
#         word = request.GET.get('q')
#         print(word)
#
#         obj = get_object_or_404(Video, id=my_str)
#         queryset = Video.objects.all().filter(title__contains=id)
#         context = {
#             'object_list': queryset,
#             "videos_number": Video.objects.all().count()
#         }
#
#         return render(request, "home.html", context)
#     else:
#         tag_set = Tag.objects.all()
#         queryset = Video.objects.all()
#         context = {
#             "tag_set": tag_set,
#             "object_list": queryset,
#             "videos_number": Video.objects.all().count()
#         }
#
#         return render(request, "home.html", context)

class UpdateVideoView(View):
    message = "None of the fields can be empty! Try again."

    def get(self, request, *args, **kwargs):
        return render(request, "upload.html")

    def post(self, request, *args, **kwargs):
        tags = request.POST.get("tags")
        title = request.POST.get("title")
        if tags and request.FILES and title:
            new_tag = Tag.objects.create(name=tags)
            new_video = Video.objects.create(title=title, file=request.FILES['video'])
            new_video_tag = VideoTag.objects.create(video=new_video, tag=new_tag)
            new_video_tag.save()
            return redirect("/tube/")
        else:
            context = {"user": request.user, "message": self.message}
            return render(request, "upload.html", context=context)


# def UpdateVideoView(request):
#     if request.method == "POST":
#         v_form = VideoForm(request.POST, request.FILES)
#         t_form = TagForm(request.POST)
#         vt_form = VideoTag
#         # vt_form = VideoTagForm(request.POST)
#         if request.user.is_authenticated:
#         # if v_form.is_valid() and t_form.is_valid():
#             video = v_form.save()
#             tag = t_form.save()
#             video_tag = VideoTag()
#
#
#             video_tag.video = video
#             video_tag.tag = tag
#             video_tag.save()
#
#             # return redirect(reverse('home_home'))
#             return redirect("/tube/")
#             # context = {}"
#             # return render(request, 'home.html', context)
#             # return HttpResponseRedirect('/tube/')
#         else:
#             context = {"user": request.user}
#             return render(request, "upload.html", context=context)
#             # return HttpResponseRedirect('/tube/')
#
#     else:
#         v_form = VideoForm
#         t_form = TagForm
#         vt_form = VideoTag
#         #
#         context = {}
#         context.update(csrf(request))
#         context['v_form'] = v_form
#         context['t_form'] = t_form
#         context['vt_form'] = vt_form
#         # print("render", render(request, 'upload.html', context))
#         # return render(request, "tube/upload.html", context)
#         return render(request, 'upload.html', context)


# class UpdateVideoView(CreateView):
#     template_name = 'upload.html'
#     v_form_class = VideoForm(prefix="v")
#     t_form_class = TagForm(prefix="t")
#     # vt_form_class = VideoTagForm
#     queryset = Video.objects.all()
#     # success_url = reverse_lazy('/tube/')
#     success_url = "/tube/"
#
#     def form_valid(self, form):
#         print(form.cleaned_data)
#         return super().form_valid(form)


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = '../login/'
    # success_url = reverse_lazy('/tube/')
    template_name = 'signup.html'


class MyLogoutView(LogoutView):
    # redirect_authenticated_user = True
    # template_name = 'login.html'
    success_url = reverse_lazy('/tube/')


class MyLoginView(LoginView):
    # redirect_authenticated_user = True
    template_name = 'login.html'
    success_url = reverse_lazy('/tube/')

    # def get_success_url(self):
    #     url = self.get_redirect_url()
    #     return url or resolve_url(settings.LOGIN_REDIRECT_URL)

    # def get_success_url(self):
    #     return reverse('home_home')

    def form_invalid(self, form):
        return HttpResponseRedirect(self.get_success_url())


def home_view(request, *args, **kwargs):
    # print(args, kwargs)
    # print(request.user)
    # return HttpResponse("<h1>Hello World</h1>")
    if request.method == 'GET':
        # print(request.GET)
        word = request.GET.get('q')
        # print(word)
        if word is not None:
            queryset = Video.objects.all().filter(title__contains=word)
            context = {
                "object_list": queryset,
                "videos_number": queryset.count()
            }
            return render(request, "home.html", context)
        word = request.GET.get('tag')
        # print("tag word", word)
        if word:
            vid = VideoTag.objects.all().filter(tag__name=word)
            # print("vid", vid)
            # print("vid.first().video", vid.first().video.title)
            queryset = Video.objects.all().filter(title=vid.first().video.title)
            context = {
                "object_list": queryset,
                "videos_number": queryset.count()
            }
            return render(request, "home.html", context)
        else:
            tag_set = Tag.objects.all()
            queryset = Video.objects.all()
            context = {
                "tag_set": tag_set,
                "object_list": queryset,
                "videos_number": Video.objects.all().count()
            }

            return render(request, "home.html", context)


def video_list_view(request):
    queryset = Video.objects.all()  # list of all ibject in the database
    context = {
        "object_list": queryset,
        "videos_number": Video.objects.all().count()
    }
    return render(request, "video_list.html", context)



# def video_filtering(request):
#
#     if request.method == 'GET':
#         word = request.GET.get('q')
#         queryset = Video.objects.all().filter(title__contains=word)
#         context = {
#             "object_list": queryset,
#             "videos_number": queryset.count()
#         }
#         return render(request, "home.html", context)

