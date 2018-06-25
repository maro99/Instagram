from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignupForm(forms.Form):
    username = forms.CharField(
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                # 'style': 'margin-bottom: 30px;',
            }
        )
    )
    email = forms.EmailField(
        label='이메일',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )
    password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )


    # form.is_valid()를 통과하지 못한 경우,
    #  유효성 검증을 통과하지 못한 내용은 form.<field>.errors에 정의됨 -> form을 순회하면 form.<field>를 하나씩 순회
    #  (통과하지 못한 경우의 'form'변수를 디버깅을 이용해 확인해본다)

    # 1. form.is_valid()를 통과하지 못했을 경우, 해당 내용을 template에 출력하도록 구현
    # 2. SignupForm의 clean()메서드를 재정의하고, password와 password2를 비교해서 유효성을 검증하도록 구현



    def clean_username(self):
        # 적절히작성
        # 원하는결과는, 중복되지 않는 username을 사용하면 유저 생성
        # 중복된 username을 입력하면 오류목록이 출력(자동)

        data = self.cleaned_data['username']

        if User.objects.filter(username=data).exists():
            raise forms.ValidationError('같은 아이디가 존재한다.')

        return data

    # def claen_pasword1(self):
    #
    #     password1_data = self.cleaned_data['password']
    #     password2_data = self.cleaned_data['password2']
    #
    #     if password_data != password2_data:
    #         raise ValidationError('두 비밀번호가 일치하지 않는다.')
    #
    #     return password_data



#clean() 매소드에 변화 안줬을때 기본 반환 값은 무엇인가?
# 1. 우리의 from이 상속받은 부모클래스가 clean()메소드 반환값에 cleaned_data dict이 없는경우.
# 2. 우리의 from이 상속받은 부모클래스가 clean()메소드 반환값이  cleaned_data dict인 경우.

# 1
#     def clean(self):
#         super().clean()
#         password = self.cleaned_data.get('password')
#         password2 = self.cleaned_data.get('password2')
#
#
#         if password != password2:
#             raise forms.ValidationError(
#                 "비밀번호 두개가 불일치 합니다."
#             )


# 2
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get('password')
#         password2 = cleaned_data.get('password2')
#
#         if password != password2:
#             raise forms.ValidationError(
#                 "비밀번호 두개가 불일치 합니다."
#             )
#
#             # self.add_error()



#form의 에러와 field에러가 다르다.from
#form의 에러는 자동으로 form위에 나오고 field에러는 템플릿에서 출력해줬다.

#field에러 처럼 처리해주자.from

    def clean(self):
        super().clean()
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')


        if password != password2:

            msg = "비밀번호 두개가 불일치 합니다."

            self.add_error('password',msg)
            self.add_error('password2',msg)