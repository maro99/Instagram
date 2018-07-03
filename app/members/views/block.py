from django.contrib.auth import get_user_model
from django.shortcuts import redirect

User=get_user_model()

__all__ = (
    'block_toggle',
)


def block_toggle(request, pk):

    if request.method == 'POST':
        from_user = request.user
        to_user = User.objects.filter(pk=pk)[0]

        if to_user in from_user.blocking:
            from_user.unblock(to_user)
        else:
            from_user.block(to_user)

    return redirect('index')


