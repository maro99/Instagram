from django.urls import path

from posts.apis import PostList

app_name = 'posts-api'

urlpatterns = [
    path('posts/', PostList.as_view())
]
