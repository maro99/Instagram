from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from pip._vendor import requests

from config import settings

User = get_user_model()


# Create your views here.
from members.forms import SignupForm


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


def withdraw(request):

    user = request.user
    logout(request)
    user.delete()
    return redirect('index')

@require_POST
# @login_required
def follow_toggle(request ,pk):
    """
    * GET요청은 처리하지 않음
    * 로그인 된 상태에서만 작동
    POST요청일 때
        1. request.POST로 'user_pk'값을 전달받음
            pk가 user_pk인 User를 user에 할당
        2. request.user의
    :param request:
    :return:
    """

    # if user in User.obejcts.filter(pk__in=post.postlike_set.value('user_id')):

    if request.method == 'POST':
        from_user = request.user
        to_user = User.objects.filter(pk=pk)[0]

        if to_user in from_user.following:
            from_user.unfollow(to_user)
        else:
            from_user.follow(to_user)
    return redirect('index')

def block_toggle(request, pk):

    if request.method == 'POST':
        from_user = request.user
        to_user = User.objects.filter(pk=pk)[0]

        if to_user in from_user.blocking:
            from_user.unblock(to_user)
        else:
            from_user.block(to_user)

    return redirect('index')




#####################################facebook login관련 함수들.#############################


def get_authentication_code(request):
    # html의 a테그의 링크
        # https://www.facebook.com/v3.0/dialog/oauth?
		# client_id=166861210842547
		# &redirect_uri=http://localhost:8000/members/facebook-login/
		# &scope=email,public_profile" class="btn btn-primary

    # 유저가 클릭하게 되면
    # 서버에서는 facebook의 outh주소로 화면을 전환하고 권한을 묻는다.
    # 권한을 수락하면 이 view와 url을 연결된 주소로 (redirect_url에 있는 주소) redirect된다.

    # 이때 GET parameter의 'code에 값이 전달(authentication code)된다.
    code = request.GET.get('code')
    return code


# 전달받은 인증코드를 사용해서 엑세스토큰을 받음.(facebook의 access_token주소로 get요청통해서)
def get_access_token(code):
    # code = get_authentication_code(request)
    url = 'https://graph.facebook.com/v3.0/oauth/access_token'

    params = {
        'client_id':settings.FACEBOOK_APP_ID,
        'redirect_uri':'http://localhost:8000/members/facebook-login/',
        'client_secret':settings.FACEBOOK_APP_SECRET_CODE,
        'code':code,
    }

    # 왼쪽 엑세스 코드교환 엔드포인터에 HTTP GET요청 하면
    # jason 반환됨.(java script object nodtaion 자바스크립트에서 객체나타내기위한표기법)
    response = requests.get(url,params)

    # jason형식 택스트를  jason parser 이용해서 python 객체(object)로반환함.
    # response_dict = json.loads(response.text)
    response_dict = response.json()

    #여기서 access_token값만 꺼네서 HttpResponse로 출력.
    access_token = response_dict['access_token']
    return access_token

# face북의 debug_token주소 에 요청 보내고 결과 받기(받은 엑세스 토큰을 debug 결과에서 해당 토큰의 user_id(사용자 고유값) 가져올 수 있음.)
# iput_token을 위의'access_token'
# access_token은 {client_id}|{client_secret} 값.
def get_debug_token(access_token):
    # access_token=get_access_token(request)

    url = 'https://graph.facebook.com/debug_token'

    params = {
        'input_token':access_token,
        'access_token':'{}|{}'.format(
            settings.FACEBOOK_APP_ID,settings.FACEBOOK_APP_SECRET_CODE
        )
    }
    response = requests.get(url, params)
    return response

# GraphAPI의 ,'me'(User) 를 이용해서  Facebook User정보 받아오기.
def get_user_info_by_GrapicAPI(access_token):
    # access_token=get_access_token(request)
    url = 'https://graph.facebook.com/v3.0/me'

    # access_token과 가져올 유저 요소를 params에 담아서 get요청한다.
    params = {
        'fields':
            ','.join(['id', 'name', 'first_name', 'last_name', 'picture']),
        'access_token': access_token,
    }
    #get요청으로 받아온 janson형태 데이터를 parser로 python형태 dic 객체로반환한다.
    response = requests.get(url, params)
    response_dict = response.json()
    return response_dict


def create_user(response_dict):
    # 받아온 정보 dic 중 회원가입에 필요한 요소들 꺼내기
    facebook_user_id = response_dict['id']
    first_name = response_dict['first_name']
    last_name = response_dict['last_name']
    url_img_profile = response_dict['picture']['data']['url']

    #가져온 userid와 동인한 id있으면 get없으면 create하고 True도 같이 반환.
    user, user_created = User.objects.get_or_create(
        username=facebook_user_id,  # 이값은 고유해서 get할때 사용 가능.
        defaults={  # 이값은 고유하지 않아도됨. 입력되는 값.
            'first_name': first_name,
            'last_name': last_name,
        }
    )
    return user


def facebook_login(request):
    code = get_authentication_code(request)
    access_token = get_access_token(code)
    response_dict =get_user_info_by_GrapicAPI(access_token)
    user = create_user(response_dict)
    login(request, user)
    return redirect('index')
