# /api/posts/
# 1. posts.serializers에 PostSerializer구현
# 2. apis.__init__
#   class PostList(APIview):
#       def get(self, request):
#           <logic>

#   3. config.urls에서 (posts.urls는 무시)
#   /api/posts/가 위의 PostList.as_view()와 연결되도록 처리.



from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import PostSerializer
from ..models import Post, Comment, PostLike
# from ..forms import CommentModelForm


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer











    # def get(self, request):
    #     posts = Post.objects.all()
    #     serializer = PostSerializer(posts, many=True)
    #     return Response(serializer.data)
    #
    #
    # def post(self, request, format=None):
    #     pass
    #
    #
    #




    #
    # def post_list(request):
    #     form = CommentModelForm()
    #     posts = Post.objects.all()
    #     comments = Comment.objects.all()
    #     postlikes = PostLike.objects.all()
    #
    #     context = {
    #         'posts': posts,
    #         'user': request.user,
    #         'form': form,
    #         'comments': comments,
    #         'postlikes': postlikes,
    #     }
    #
    #     return render(request, 'posts/post_list.html', context)






###이하는 과해서 일단 위처럼 하기로함.

# /posts/ <- posts.views.post_list
# /api/posts/ <-posts.apis.PostList.as_view

# 1. posts.serializers에 PostSerializer구현
# 2. api에 PostList GenericCBV 구현
# 3.posts.urls를 분할
#       -> posts.urls.views
#       -> posts.urls.apis
# 4. config.urls.에서 적절히 include 처리
# 5. /api/posts/로 Postman Collection작성
# 6. 잘되나 확인.