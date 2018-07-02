from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404
User = get_user_model()

from django.views.decorators.http import require_POST

from ..models import Post, Comment, PostLike



__all__ = (
    'post_like',
)


@login_required
def post_like(request, pk):

    if request.method == 'POST':
        user = request.user
        post = Post.objects.get(pk = pk)

        if user in post.post_like_users:
        # if user in User.obejcts.filter(pk__in=post.postlike_set.value('user_id')):
            PostLike.objects.filter(user=user, post =post).delete()
            post.likes -= 1
            post.save()

        else:
            postlike=PostLike(
                user = user,
                post = post,
            )
            postlike.save()
            post.likes +=1
            post.save()



    return redirect('index')








