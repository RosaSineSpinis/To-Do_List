"""hypertube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tube.views import home_view, video_list_view, video_detail_view,\
    MySignupView, MyLoginView, UpdateVideoView, MyLogoutView, video_raw_view
#tag_filter_video

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('tube/upload/', UpdateVideoView.as_view(), name='upload'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('signup/', MySignupView.as_view(), name='signup'),
    # path('tube/<str:my_str>/', tag_filter_video, name='tag_filter_video'),
    path('tube/<str:my_str>/', video_raw_view, name='video_raw_view'),
    path('tube/watch/<int:my_id>/', video_detail_view, name='video_detail'),
    path('video_list/', video_list_view, name='video_list_view'),
    path('tube/', home_view, name='home_home'),
    # path('tube/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)