from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from accounts.models import User
from .models import Review
from .serializers import ReviewSerializer
from .pagination import ReviewPagination


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = ReviewPagination

    @action(detail=False)
    def sender(self, request):
        qs = self.queryset.filter(send_id=request.GET['id'])
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def receiver(self, request):
        qs = self.queryset.filter(receive_id=request.GET['id'])
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)


