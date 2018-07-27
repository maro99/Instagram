from django.urls import path

from ..apis import PostList

app_name = 'posts-api'

urlpatterns = [
    path('', PostList.as_view()),
]
