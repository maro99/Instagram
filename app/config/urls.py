"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from members.apis import UserList
from posts.apis import PostList
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls.views')),# 맞나?
    path('members/',include('members.urls.views')), # 맞나?
    path('', views.index, name='index'),

    path('api/',include('posts.urls.apis' )),  # 두개 합치면 앞에서만 찾고 실패시 뒤는 참조안함.
    path('api/', include( 'members.urls.apis', ))
    # path('api/posts/',PostList.as_view()),
    # path('api/users/', UserList.as_view())

   # path('media/' )
] + static(
    prefix= settings.MEDIA_URL,
    document_root = settings.MEDIA_ROOT,
)


#   3. config.urls에서 (posts.urls는 무시)
#   /api/posts/가 위의 PostList.as_view()와 연결되도록 처리.