from django.urls import path

from . import views


urlpatterns = [
    path('',views.post_list,name = 'index'),
    path('<int:pk>/',views.post_detail,name='detail'),
]

