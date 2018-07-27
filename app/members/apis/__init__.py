# /api/users/
# 1. members.serializers에 UserSerializer구현
# 2. apis.__init__
#   class UserList(generics.ListAPIview):
#       def get(self, request):
#           <logic>

#   3. config.urls에서
#   /api/users/가 위의 UserList.as_view()와 연결되도록 처리.
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.response import Response


from ..serializers import UserSerializer
User = get_user_model()

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer




