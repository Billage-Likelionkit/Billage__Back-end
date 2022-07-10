from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet

router = DefaultRouter()
router.register('review', ReviewViewSet)

review = ReviewViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })
review_send_list = ReviewViewSet.as_view({
        'get': 'list',
    })
review_receive_list = ReviewViewSet.as_view({
        'get': 'list',
    })
review_detail = ReviewViewSet.as_view({
        'get': 'retrieve',
        'delete': 'destroy',
    })

urlpatterns = [
    path('', include(router.urls)),
    path('review/', review),
    path('review/<int:id>/', review_detail),
    path('review/sender/', review_send_list),
    path('review/receiver/', review_receive_list),
]