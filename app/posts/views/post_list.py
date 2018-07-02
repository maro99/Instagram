from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404

from posts.forms import CommentModelForm

User = get_user_model()

from django.views.decorators.http import require_POST

from ..models import Post, Comment, PostLike



__all__ = (
    'post_list',
)


def post_list(request):

    form = CommentModelForm()

    posts =Post.objects.all()

    comments = Comment.objects.all()

    postlikes = PostLike.objects.all()

    context={
        'posts': posts,
        'user':request.user,
        'form':form,
        'comments':comments,
        'postlikes':postlikes,
    }

    return render(request,'posts/post_list.html',context)
