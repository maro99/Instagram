from django.contrib.auth import logout
from django.shortcuts import redirect

__all__=(
    'logout_view',
)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('posts:post-list')
    else:
        return redirect('posts:post-list')

