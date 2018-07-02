from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404
User = get_user_model()

from django.views.decorators.http import require_POST

from ..models import Post, Comment, PostLike


__all__ = (
    'post_delete',
)



@login_required
@require_POST
def post_delete(request,pk):

    post = get_object_or_404(Post, pk = pk)
    if post.author != request.user:
        raise PermissionDenied('지울 권한이 없습니다.')
    post.delete()

    return redirect('posts:post-list')


# #위 두개의 decorator 없이 구현해보자.
# def post_delete(request,pk):
#
#     if request.method =='POST':
#         return HttpResponseNotAllowed()
#
#     if not request.user.is_authenticated:
#         return redirect('members:login')
#
#     #나머지는 같다.