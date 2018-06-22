from django.http import HttpResponse
from django.shortcuts import render


#post_list(request)
#post_detail(request, pk) <_ view parameter 및 path 패턴명에 pk 사용

#구현하세요
#base.html기준으로.
#   TEMPLATE설정 쓸 것 (templates폴더를 DIRS예 추가)
#                           -->경로이름은 TEMPLATES_DIR로 settings.py의 윗부분에 추가

#post_list는 'posts/post_list.html'
#post_detail은  'post/post_detail.html' 사용

#1. view와 url 연결 구현
#2. view 에서 template을 렌더링 하는 기능 추가
#3. templates에서 QuerySet 또는 objects를 사용해서 객체 출력
#4. template에 extend 사용



def post_list(request):

    return HttpResponse( 'post-list')

def post_detail(request,pk):

    return HttpResponse('post-detail')