from django.urls import path
from ..import views

app_name = 'posts'

urlpatterns = [
     path('', views.post_list, name='post-list'),
     path('<int:pk>/', views.post_detail, name='post-detail'),
     path('create/',views.post_create, name='post-create'),
     path('<int:pk>/delete/',views.post_delete, name='post-delete'),
     path('<int:pk>/comment/',views.post_comment, name='post-comment'),
     path('<int:pk>/like/', views.post_like, name = 'post-like'),
]

