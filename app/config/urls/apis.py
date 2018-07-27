from django.urls import path, include

urlpatterns = [
    # api
        path('posts/', include('posts.urls.apis')),
        path('users/', include('members.urls.apis')),
]
