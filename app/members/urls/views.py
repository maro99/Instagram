from django.urls import path
from ..import views


app_name = 'members'

urlpatterns = [

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('signup/', views.signup_view, name = 'signup'),

    path('signup/', views.signup, name = 'signup'),
    path('withdraw/',views.withdraw, name='withdraw'),

    path('<int:pk>/follow/',views.follow_toggle,name='follow-toggle'),
    path('<int:pk>/block/', views.block_toggle, name='block-toggle'),
    path('facebook-login/', views.facebook_login,name='facebook-login'),
]