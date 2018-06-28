from django.conf import settings
from django.db import models

from members.models import User

#posts 앱의 class Post
#   author settings.AUTH_USER_MODE
#   photo (ImageField)
#   content (Text)
#   created_at(DateTime)

# 를 작성하고 migrate
# ImageField를 위해서 Pillow라이버러리 필요 설치할것.


class Post(models.Model):
    author =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete= models.CASCADE)

    photo = models.ImageField(upload_to= 'post', blank=True) #이미지필드는 파일필드 상속 받음. 추가로 가로세로정보 들어감.
                                                            # 어디로 갈지 upload_to 설정함.
    content = models.TextField(blank =True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =['-pk']


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        null=True,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    content = models.CharField(max_length=300, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class PostLike(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
