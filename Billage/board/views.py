from multiprocessing import AuthenticationError
from django.shortcuts import render
from .models import Board
from .serializers import BoardSerializer
from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView

# Create your views here.
class BoardViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def perform_create(self,serializer):
        serializer.save(board = self.request.board)

class BoardListAPI(ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer