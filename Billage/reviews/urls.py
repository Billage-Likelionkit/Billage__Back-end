from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet

router = DefaultRouter()
router.register('review', ReviewViewSet)

review = ReviewViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })
review_list = ReviewViewSet.as_view({
        'get': 'list',
    })

review_detail = ReviewViewSet.as_view({
        'get': 'retrieve',
        'delete': 'destroy',
    })

"""
@action(detail=True, methods=['get'])
def set_password(self, request, pk=None):
    user = self.get_object()
    serializer = PasswordSerializer(data=request.data)
    if serializer.is_valid():
        user.set_password(serializer.validated_data['password'])
        user.save()
        return Response({'status': 'password set'})
    else:
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

"""
urlpatterns = [
    path('', include(router.urls)),
    path('review/', review),
    path('review/<int:id>/', review_detail),
    path('review/sender/<int:user_id>/', review_list),
    path('review/receiver/<int:user_id>/', review_list),
]