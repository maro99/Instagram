
from django import forms
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from posts.models import Post

User=get_user_model()

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








