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

# from ..serializers import PostSerializer ###############
from ..serializers import PostListSerializer


# 과제 위해 일단 주석처리 해 놓음

# from ..models import Post, Comment, PostLike
# # from ..forms import CommentModelForm
#
#
# class PostList(generics.ListAPIView):
#     queryset = Post.objects.all()
#     # serializer_class = PostSerializer##########
#     serializer_class = PostListSerializer
#


from ..serializers import PostListSerializer, PostDetailSerializer
from ..models import Post


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

    def get_serializer_class(self):
        # GET, POST요청 (List, Create)시마다 다른 Serializer를 쓰도록
        # get_serializer_class()를 재정의
        if self.request.method == 'GET':
            return PostListSerializer
        elif self.request.method == 'POST':
            return PostDetailSerializer

    def perform_create(self, serializer):
        # PostListSerializer로 전달받은 데이터에
        # 'owner'항목에 self.request.user데이터를 추가한 후
        # save() 호출, DB에 저장 및 인스턴스 반환
        serializer.save(author=self.request.user)

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