"""
URL configuration for Backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from rest_framework import routers
from Backend.views import CommentView, UserLikeView, UserView
from Backend.views.PostView import PostView
from Backend.views.NoteView import NoteView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'posts', PostView, "post")
router.register(r'comments', CommentView, "comment")
router.register(r'users', UserView, "user")
router.register(r'userlikes', UserLikeView, "userlike")
router.register(r'notes', NoteView, "note")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
