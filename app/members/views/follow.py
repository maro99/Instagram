from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.views.decorators.http import require_POST

__all__ =(
    'follow_toggle',
)


User = get_user_model()
@require_POST
# @login_required
def follow_toggle(request ,pk):
    """
    * GET요청은 처리하지 않음
    * 로그인 된 상태에서만 작동
    POST요청일 때
        1. request.POST로 'user_pk'값을 전달받음
            pk가 user_pk인 User를 user에 할당
        2. request.user의
    :param request:
    :return:
    """

    # if user in User.obejcts.filter(pk__in=post.postlike_set.value('user_id')):

    if request.method == 'POST':
        from_user = request.user
        to_user = User.objects.filter(pk=pk)[0]

        if to_user in from_user.following:
            from_user.unfollow(to_user)
        else:
            from_user.follow(to_user)
    return redirect('index')
