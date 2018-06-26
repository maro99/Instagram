from django.contrib.auth import authenticate, login, logout, get_user_model



from django.http import HttpResponse
from django.shortcuts import render, redirect

User = get_user_model()


# Create your views here.
from members.forms import SignupForm


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


# def signup_view(request):
#
#
#     if request.method =='POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         user = User.objects.create_user(username ,email, password)
#         login(request, user)
#
#         return redirect('posts:post-list')
#     else:
#         return render(request, 'members/signup.html')

#User 클래스를 가져올때는 get_user_model()
#Foreignkey에 User모델을 지정할 때는 settings.AUTH_USER_MODEL
# User.get_user_model()

# def signup(request):
#
#     if request.method == 'POST':
#
#
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         password2 = request.POST['password2']

        # 2번째 검사로, password와 password2가 같은지 검사
        # 다를경우 해당 오류를 출력
        #
        # username 도 이미 존재하고 password도 다를 경우 둘다 출력


        # exist를 사용해서  유저가 이미 존재하면 signup으로 다시 redirect
        # 존재하지 않는 경우에만 아래 로직 실행.

        # if password != password2:
        #     context['erros'].append('password와 password2가 같지않다.')

    #  내가한 부분)
    #     if User.objects.filter(username=username).exists() or password != password2:
    #         # 단순 redirect가 아니라 render를 사용.
    #         # render에 context를 전달
    #         #   context로 사용할 dict 객체의
    #         #       'errors' 키에 List를 할당하고 해당 리스트에
    #         #          '유저가이미존재함' 문자열을 추가해서 전달.
    #         #   탬플릿에서는 전달받은 errors를 순회하며 애러메시지를 출력
    #
    #
    #         context={
    #             'errors':[],
    #             'username':username,
    #             'email':email,
    #             'password':password,
    #         }
    #
    #         if User.objects.filter(username=username).exists():
    #             context['errors'].append('유저가이미존재')
    #
    #         if password != password2:
    #             context['errors'].append('password와 password2가 같지않다.')
    #
    #         return render(request,'members/signup.html', context)
    #     else:
    #         user = User.objects.create_user(username = username , email = email, password = password)
    #         login(request, user)
    #         return redirect('index')
    #
    # else:
    #     return render(request, 'members/signup.html')
    #
    #

        #     context={
    #         'errors':[],
    #         'username':username,
    #         'email':email,
    #         'password':password,
    #     }
    #
    #     if User.objects.filter(username=username).exists():
    #         context['errors'].append('유저가이미존재')
    #
    #     if password != password2:
    #         context['errors'].append('password와 password2가 같지않다.')
    #
    #     if context['errors']:
    #         return render(request,'members/signup.html', context)#@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #
    #     else:
    #         user = User.objects.create_user(username = username , email = email, password = password)
    #         login(request, user)
    #         return redirect('index')
    #
    # else:
    #     return render(request, 'members/signup.html')#@@@@@@@@@@@@@@@@@@@@@@@@








    # 중복 없에봄. return render 위아래 합치고 싶다.
    # post요청 오면~ error존제시 아래에서 render를 사고 싶다.


def signup_bak(request):
    context = {
        'errors': [],
    }
    if request.method == 'POST':

        # username, email, password, password2에 대해서
        # 입력되지 않은 필드에 대한 오류를 추가

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']


        # if not username:
        #     context['errors'].append('usname 입력 안됨')
        # if not email:
        #     context['errors'].append('email 입력 안됨.')
        # if not password:
        #     context['errors'].append('password 입력 안됨')
        # if not password2:
        #     context['errors'].append('password2 입력 안됨')


        #for 문으로 작동하도록 수정
        #locals()사용해라.
        # 일단은 이렇게 하면 되지만 맘에 안든다.
        # for문으로 하고싶다. 필요한 필드들만 검사하고 싶다.
        # print(locals())  ---> 스코프 안의 변수들 나타냄.


        # required_fields = ['username','email','password','password2']
        #
        # for filed_name in required_fields:
        #     if not locals()[filed_name]:
        #         context['errors'].append('{}을(를) 체워주세요'.format(filed_name))


        #for문 에서 if문 없이 친절하게 한글로 error문을 context에 넣어주자.requritefields-->dict

        # required_fields = {'username':'유저이름','email':'이메일','password':'페스워드','password2':'패스워드2'}
        required_fields = {'username':
                               {'verbose_name':'유저이름'},
                           'email':
                               {'verbose_name': '이메일 '},
                           'password':
                               {'verbose_name': '비밀번호1'},
                           'password2':
                               {'verbose_name': '비밀번호2'},
                           }


        for field_name in required_fields:
            if not locals()[field_name]:
                context['errors'].append('{}을(를) 체워주세요'.format(
                    required_fields[field_name]['verbose_name']
                ))







        # 입력데이터 채워넣기
        context['username'] = username
        context['email'] = email

        # form에서 전송된 데이터들이 올바른지 검사


        if User.objects.filter(username=username).exists():
            context['errors'].append('유저가 이미 존재함')
        if password != password2:
            context['errors'].append('패스워드가 일치하지 않음')

        # errors가 없으면 유저 생성 루틴 실행
        if not context['errors']:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
            )
            login(request, user)
            return redirect('index')
    return render(request, 'members/signup.html', context)



# form에서 지금까지 것들 이뤄지는데 장고 Forms~에서 지원하는 것이다.
# Form 문서를 봐라 --->문서타고간것 동영상 참고.

from members.forms import SignupForm

def signup(request):

    if request.method == 'POST':

        form = SignupForm(request.POST)

        # form에 들어있는 데이터가 유효한지 검사.(해당 form 클래스에서 정의한 데이터 형식에서 벋어나지 않는지 판단.)
        if form.is_valid():
            # 유효할 경우 유저 생성 및 redirect
            # username 존재하는지
            # password, password2 같은지 추가로 검사헤 줘야함.

            # is_vaild()가 True를 반환하면 유효성이 검사 된 양식 데이터는 form.clened_data사전에 저장된다.
            # username = form.cleaned_data['username']
            # email =  form.cleaned_data['email']
            # password = form.cleaned_data['password']
            #
            # user=User.objects.create_user(
            #     username=username,
            #     email=email,
            #     password=password,
            # )

            # 위의 내용들을 아래에 다 담아버리자.

            user = form.signup() #signup 메소드는 form의 메소드 인데 form은 signupForm클래스의 인스턴스이다.

            login(request,user)
            return redirect('index')

        else:
            result = '\n'.join(['{}:{}'.format(key,value) for key, value in form.errors.items()])
            return HttpResponse(result)
            # context = {'form': form, }
            # return render(request, 'members/signup.html', context)


    else:
        form = SignupForm()
        context = {'form': form,}
        return render(request, 'members/signup.html', context)


