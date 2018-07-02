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
    'post_comment',
)



@login_required
def post_comment(request,pk):

    if request.method =='POST':
        form = CommentModelForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(pk=pk)
            comment.user = request.user
            comment.save()

    return redirect('index')


