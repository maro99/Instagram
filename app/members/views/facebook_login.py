import requests
from django.contrib.auth import get_user_model, login, authenticate
from django.shortcuts import redirect

from config import settings

__all__ =(
    'facebook_login',
)

User = get_user_model()




def facebook_login(request):

    code = request.GET.get('code')
    user = authenticate(request, code=code)

    if user is not None:
        login(request, user)
        return redirect('index')
    return redirect('members:login')