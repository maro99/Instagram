from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.


def login_view(request):

    # 1. member.urls <_ 'members/'로 include되도록 config.urls 모듈에 추가.
    # 2. pathh구현 URL: '/members/login/'
    # 3. path와 이 view연결
    # 4. 일단 잘 나오는지 확인
    # 5. 잘 나오면 form을 작성(username, password를 받는 input2개)

    # 6. form 작성후에는 POST방식 요청을 보내서 이 뷰에서 request,POST요청이 잘 왔는지 확인
    # 7. 일단은 받은 username ,password값을 HttpResponse에 보여주도록 한다.


    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #받은 username과 password에 해당하는 User가 있는지 인증.
        user = authenticate(request, username=username, password=password)

        #인증에 성공한 경우
        if user is not None:
            #세션값을 만들어 DB예 저장하과 HTTP response의 Cookie에 해당값을 담아보내도록 하는
            #login()함수를 실행한다.
            login(request, user)
            #dlgn post-list로 redirect
            return redirect('posts:post-list')
        #인증에 실패한 경우 (username또는 password가 틀린경우)
        else:
            #다시 로그인 페이지로 redirect
            return redirect('members:login')

        #인증에 성공하면 post:post-list로 이동
        #실패하면 다시 members:login으로 이동.

    #GET 요청일 경우
    else:
        return render(request, 'members/login.html')


def logout_view(request):
    if request.method =='POST':

        logout(request)
        return redirect('posts:post-list')
    else:
        return redirect('posts:post-list')


def signin_view(request):


    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username ,email, password)
        login(request, user)

        return redirect('posts:post-list')
    else:
        return render(request, 'members/signup.html')