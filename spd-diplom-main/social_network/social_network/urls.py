"""
URL configuration for social_network project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
#from xml.dom.minidom import Comment

#import path
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from posts.views import PostView,LikeView,Post_1View
from rest_framework.response import Response
from posts.views import APIView
from rest_framework import viewsets
from rest_framework import routers, serializers, viewsets
#from dj_rest_auth.registration.views import RegisterView
#from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView
from django.urls import path


#from rest_framework.views import LikeView,PostView,CommentView




router = routers.DefaultRouter()

#router.register('post',PostView,  basename='post',)
#router.register('comment',CommentView,  basename='comment',)
#router.register('like',LikeView,  basename='like',)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('post/', PostView.as_view()),
    path('like/',LikeView.as_view()),
    path('comment/',Post_1View.as_view()),

]
#path('api/post', PostView.as_view()),
    #path('api/', include(''.urls.authtoken')),  # Работа с токенами


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#
    #path('user'/ 'user'.title.urls)]
#if settings.DEBUG:
    #urlpatterns += static(settings.MEDIA_URL,
                         # document_root=settings.MEDIA_ROOT)]
#