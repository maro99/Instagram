from rest_framework import generics

# from ..serializers import PostSerializer
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



# class PostList(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
