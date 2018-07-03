from django.contrib.auth import login, get_user_model
from django.shortcuts import redirect, render

from members.forms import SignupForm
User = get_user_model()


def signup(request):

    if request.method == 'POST':

        form = SignupForm(request.POST,request.FILES)

        # form에 들어있는 데이터가 유효한지 검사.(해당 form 클래스에서 정의한 데이터 형식에서 벋어나지 않는지 판단.)
        if form.is_valid():

            user = form.signup() #signup 메소드는 form의 메소드 인데 form은 signupForm클래스의 인스턴스이다.

            login(request,user)
            return redirect('index')

    else:
        form = SignupForm()

    context = {'form': form, }
    return render(request, 'members/signup.html', context)






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




######################################과거코드들... 일단 주석처리함.###################################3

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



