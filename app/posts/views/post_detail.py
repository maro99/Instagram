from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404
User = get_user_model()

from django.views.decorators.http import require_POST

from ..models import Post, Comment, PostLike


__all__ = (
    'post_detail',
)

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'posts/post_detail.html', context)


from posts.forms import PostForm, PostModelForm, CommentModelForm
