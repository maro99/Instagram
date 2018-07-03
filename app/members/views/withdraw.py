from django.contrib.auth import logout
from django.shortcuts import redirect

__all__=(
    'withdraw',
)

def withdraw(request):

    user = request.user
    logout(request)
    user.delete()
    return redirect('index')
