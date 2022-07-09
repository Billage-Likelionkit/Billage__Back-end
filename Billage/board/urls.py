from django.urls import path, include
from .views import BoardViewSet,BoardListAPI
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
# 첫 번째 인자는 url의 prefix
# 두 번째 인자는 ViewSet
router.register('board', BoardViewSet)

# 게시글 목록 보여주기 + 새로운 게시글 생성
board_list = BoardViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

# 게시글 상세 페이지 보여주기  + 삭제
board_detail = BoardViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy',
})

urlpatterns =[
    path('', include(router.urls)),
    path('list/', BoardListAPI.as_view()),
    path('board/', board_list),
    path('board/<int:pk>/', board_detail),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



