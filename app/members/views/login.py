from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

__all__=(
    'login_view',
)


def login_view(request):
    # 1. POST요청이 왓는뗴,요청이 올바르면서 < 코드에서 어느 위치인지 파악.
    # 2. GET parameter 에 next값이 존재할 경우<-- GET parameter는 request로 접근
    # 3. 해당값 url으로 redirect  <--redirect()함수는 URL문짜열로또 이동 가능
    # 4. next값이 존재하지 않으면 원래 이동하던 곳으로 그대로 redirect < 문자열 있는지 없는지 if로 판단.



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
            #세션값을 만들어 DB예 저장하과 HTTP response의 Cookie에 해당값을 담아보내도록 하는g
            #login()함수를 실행한다.
            # session_id 값을  django_sessions테이블에 저장, 데이터는user와 연결됨
            # 이 함수 실행 후 돌려줄 HTTP Response에는 Set-Cookie헤더를 추가, 내용은 sessionid=<session값>
            login(request, user)
            #dlgn post-list로 redirect

            #GET parameter에 'next'값이 전달되면 해당 값으로 redirect
            if request.GET.get('next'):
                return redirect(request.GET['next'])

            #next값이 전달되지 않으면 post-list로 redirect
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