from django.http import HttpResponse
from django.shortcuts import render, redirect

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

from .models import Post



def post_list(request):

    posts =Post.objects.all()
    context={
        'posts': posts
    }

    # return HttpResponse( 'post-list')
    return render(request,'posts/post_list.html',context)



def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'posts/post_detail.html', context)


from posts.forms import PostForm


def post_create(request):
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
            post = form.create_post(user_input)
            return HttpResponse('Post created')

    else:
        form = PostForm()

    context = {'form': form, }
    return render(request, 'posts/post_create.html',context)



