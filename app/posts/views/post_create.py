from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404

from posts.forms import PostForm, PostModelForm

User = get_user_model()

from django.views.decorators.http import require_POST

from ..models import Post, Comment, PostLike




@login_required
def post_create(request):
    # PostModelForm만들어서 기존과 같은역활 하게 하자.
    #   form = PostModelForm(request.POST, request.FILES)
    #   post = form.save(commit=False)
    #   post.author = request.user
    #   post.save()

    if request.method == 'POST':
        form =PostModelForm(request.POST, request.FILES)

        if form.is_valid():
            # 이전에 form 객체 생성하고 save 한 방식과 유사.
            post= form.save(commit=False) # author 없는 상태여서 save안된다. 일단 commit=False로 인스턴스 생성만하고 save안한다.
            post.author = request.user  # author 필드 우리가 넣어준다.(여기다 안빼고 PostModelForm에 넣으면 글쓰는사람이 author선택 가능해짐)
            post.save()
            return redirect('posts:post-list')
    else:
        form = PostModelForm()

    context = {'form':form, }
    return render(request, 'posts/post_create.html',context)


@login_required
def post_create_bak(request):
    # 새 포스트를 만들기
    # 만든 후에는 해당하는 post_detail로 이동
    # forms.py에 PostForm을 구현해서 사용 .

    # bound form
    # PostForm(request.POST)
    # PostForm(request.POST, request.FILES)

    # POST method 에서는 생성후 redirect
    # GET method 에서는 form이 보이는 템플릿 렌더링


    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            user_input = request.user
            form.create_post(user_input)
            return redirect('posts:post-list')

    else:
        form = PostForm()

    context = {'form': form, }
    return render(request, 'posts/post_create.html',context)
