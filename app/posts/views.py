from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404

#post_list(request)
    # /posts/
#post_detail(request, pk) <_ view parameter 및 path 패턴명에 pk 사용
    # /posts/3/

#구현하세요
#base.html기준으로.
#   TEMPLATE설정 쓸 것 (templates폴더를 DIRS예 추가)
#                           -->경로이름은 TEMPLATES_DIR로 settings.py의 윗부분에 추가

#post_list는 'posts/post_list.html'
#post_detail은  'post/post_detail.html' 사용

#1. view와 url 연결 구현
#2. view 에서 template을 렌더링 하는 기능 추가
#3. templates에서 QuerySet 또는 objects를 사용해서 객체 출력
#4. template에 extend 사용
from django.views.decorators.http import require_POST

from .models import Post



def post_list(request):



    posts =Post.objects.all()
    context={
        'posts': posts,
        'user':request.user,
    }

    # return HttpResponse( 'post-list')
    return render(request,'posts/post_list.html',context)



def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'posts/post_detail.html', context)


from posts.forms import PostForm, PostModelForm


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




























