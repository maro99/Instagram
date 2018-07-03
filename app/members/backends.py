import requests
from django.contrib.auth import get_user_model

from config import settings
from members.views import facebook_login

User = get_user_model()


class FacebookBackend:
    def authenticate(self,request,code):
        '''
        Facebook의 Authorization Code가 주어졌을때
        적절히 처리해서
        facebook의 user_id 에 해당하는 User가 있으면 해당 USer를 리턴
        없으면 생성해서 리턴.
        :param request: View의 HttpRequest object
        :param code: Facebook Aurhorization Code
        :return: User 인스턴스.
        '''

        # 전달받은 인증코드를 사용해서 엑세스토큰을 받음.(facebook의 access_token주소로 get요청통해서)
        def get_access_token(code):
            # code = get_authentication_code(request)
            url = 'https://graph.facebook.com/v3.0/oauth/access_token'

            params = {
                'client_id': settings.FACEBOOK_APP_ID,
                'redirect_uri': 'http://localhost:8000/members/facebook-login/',
                'client_secret': settings.FACEBOOK_APP_SECRET_CODE,
                'code': code,
            }

            # 왼쪽 엑세스 코드교환 엔드포인터에 HTTP GET요청 하면
            # jason 반환됨.(java script object nodtaion 자바스크립트에서 객체나타내기위한표기법)
            response = requests.get(url, params)

            # jason형식 택스트를  jason parser 이용해서 python 객체(object)로반환함.
            # response_dict = json.loads(response.text)
            response_dict = response.json()

            # 여기서 access_token값만 꺼네서 HttpResponse로 출력.
            access_token = response_dict['access_token']
            return access_token

        # face북의 debug_token주소 에 요청 보내고 결과 받기(받은 엑세스 토큰을 debug 결과에서 해당 토큰의 user_id(사용자 고유값) 가져올 수 있음.)
        # iput_token을 위의'access_token'
        # access_token은 {client_id}|{client_secret} 값.
        def get_debug_token(access_token):
            '''
            강사님 주석--->
            주어진 token을 Facebook의 debug_token API Endpoint를 사용해서 검사.
            :param access_token:
            :return: Jason응답을 parsing한 파이썬 object
            '''
            url = 'https://graph.facebook.com/debug_token'

            params = {
                'input_token': access_token,
                'access_token': '{}|{}'.format(
                    settings.FACEBOOK_APP_ID, settings.FACEBOOK_APP_SECRET_CODE
                )
            }
            response = requests.get(url, params)
            return response

        # GraphAPI의 ,'me'(User) 를 이용해서  Facebook User정보 받아오기.
        def get_user_info_by_GrapicAPI(access_token):  # , fields=None
            # 동적으로 params의 fields값을 채울 수 있도록 매개변수 및 함수 내 동작 변경.
            '''
            강사님 주석--->
            주어진 token에 해당하는 FacebooK User의 정보를 리턴.
            :param access_token:
            :return:fields: join()을 사용해 문자열을 만들 Sequence객체
            '''

            # if fields:
            #     pass
            # else:
            #     fields =  ['id', 'name', 'first_name', 'last_name', 'picture']

            url = 'https://graph.facebook.com/v3.0/me'

            # access_token과 가져올 유저 요소를 params에 담아서 get요청한다.
            params = {
                'fields':
                    ','.join(['id', 'name', 'first_name', 'last_name', 'picture']),
                'access_token': access_token,
            }
            # get요청으로 받아온 janson형태 데이터를 parser로 python형태 dic 객체로반환한다.
            response = requests.get(url, params)
            user_info_dict = response.json()
            return user_info_dict

        def create_user_from_facebook_user_info(response_dict):
            '''
            강사님주석
            Facebook GraphAPI의 'User'에 해당하는 응답인 user_info로부터
            id, first_name, last_name, picture항목을 사용해서
            Django의 User를 가져오거나 없는경우 새로 만듬(get_or_create)
            :param user_info_dict: Facebook GraphAPI -User응답.
            :return:
            '''
            # 받아온 정보 dic 중 회원가입에 필요한 요소들 꺼내기
            facebook_user_id = response_dict['id']
            first_name = response_dict['first_name']
            last_name = response_dict['last_name']
            url_img_profile = response_dict['picture']['data']['url']

            # 가져온 userid와 동인한 id있으면 get없으면 create하고 True도 같이 반환.
            return User.objects.get_or_create(
                username=facebook_user_id,  # 이값은 고유해서 get할때 사용 가능.
                defaults={  # 이값은 고유하지 않아도됨. 입력되는 값.
                    'first_name': first_name,
                    'last_name': last_name,
                }
            )


        access_token = get_access_token(code)
        user_info_dict = get_user_info_by_GrapicAPI(
            access_token)  # ,fields=['id', 'name', 'first_name', 'last_name', 'picture']
        user, user_created = create_user_from_facebook_user_info(user_info_dict)

        return user


    def get_user(self, user_id):
        '''
        user_id(primary_key)값이 주어졌을때
        해당 User가 존재하면 반환하고 없으면 None을 반환한다.
        :param user_id: User모델의 primary_key값.
        :return: primary_key에 해당하는 USer가 존재하면 Userdl인스턴스 아니면 None
        '''

        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None