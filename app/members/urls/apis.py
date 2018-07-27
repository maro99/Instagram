from django.urls import path

from members.apis import UserList

app_name = 'members-api'

urlpatterns =[
    path('users/', UserList.as_view()),

]