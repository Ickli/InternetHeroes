"""
URL configuration for InternetHeroes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from . import settings

from users.views import *
from teams.views import *

router = routers.DefaultRouter()
router.register('users', UserViewset, 'user')
router.register('add_info', AdditionalInfoViewset, 'add_info')
router.register('teams', TeamViewset, 'team')
router.register('images', UserImageViewset, 'image')
router.register('teamimages', TeamImageViewset, 'teamimage')
router.register('groups', GroupViewset, 'group')

like_view = LikeViewset.as_view({"post": "create", "delete": "destroy"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include((router.urls, 'users'), namespace='users-teams')),
    path('like/<int:pk>/', like_view),
    path('usernames/<str:login>', UserByLoginView.as_view()),
    path('checkauth/<str:login>/<str:password>', CheckAuth.as_view()),
    path('userimages/<str:login>', UserImagesView.as_view()),
    path('teamimages_of/<int:pk>', TeamImagesView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
