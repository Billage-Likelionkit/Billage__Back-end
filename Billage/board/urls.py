from django.urls import path, include
from .views import BoardViewSet,BoardListAPI,BoardcommentsViewSet,BoardcommentsListAPI,BoardcommentsDetailAPI
from django.conf import settings
from django.conf.urls.static import static


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

board_comments_list = BoardcommentsViewSet.as_view({
    'get':'list',
    'post':'create',
})

board_comments_detail = BoardcommentsViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy',
})

urlpatterns =[
    #path('', include(router.urls)),
    path('list/', BoardListAPI.as_view()),
    path('board/', board_list),
    path('board/<int:pk>/', board_detail),
    path('comments_list/', BoardcommentsListAPI.as_view()),
    path('board_comments/', board_comments_list),
    # path('board_comments/<int:pk>/', board_comments_detail),
    path('board_comments/<int:pk>/', BoardcommentsDetailAPI.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
