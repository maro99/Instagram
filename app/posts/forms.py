
from django import forms
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from posts.models import Post, Comment, PostLike

User=get_user_model()




class PostModelForm(forms.ModelForm):
    # filed 정의를 직접 하지 않음
    # 어떤 filed를 사용할 것인지만 class Meta에 기록.

    class Meta:
        model = Post
        # author 는 지워야 한다. 작성자가 선택하는 것만 넣는다.
        fields = ['photo','content',]


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']



class PostForm(forms.Form):

    photo = forms.ImageField(
        label='제목',
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
            }
        )
    )


    content = forms.CharField(
        label='내용',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )


    def create_post(self,user_input):
        photo =  self.cleaned_data['photo']
        content = self.cleaned_data['content']

        post =Post.objects.create(
            author = user_input,
            photo = photo,
            content = content,
        )

        return post







# class PostForm(forms.Form):
#
#     file = forms.FileField()








