from multiprocessing import AuthenticationError
from django.shortcuts import render
from .models import Board, Board_comments
from .serializers import BoardSerializer, BoardcommentsSeriallizer
from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class BoardViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    #def perform_create(self,serializer):
     #   serializer.save(board = self.request.board)

class BoardListAPI(ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class BoardcommentsViewSet(viewsets.ModelViewSet):
    queryset = Board_comments.objects.all()
    serializer_class = BoardcommentsSeriallizer

    # 최상위 댓글(board_id=None)을 이용해 하위 댓글을 불러옴.
    #def get_queryset(self):
     #   queryset = Board_comments.objects.all()

class BoardcommentsListAPI(ListAPIView):
    queryset = Board_comments.objects.all()
    serializer_class = BoardcommentsSeriallizer

class BoardcommentsDetailAPI(APIView):
    def get_object(self, pk):
        return get_object_or_404(Board_comments, pk=pk)

    def get(self, request, pk):
        boardcomments = self.get_object(pk)
        serializer = BoardcommentsSerializer(boardcomments)
        boardcomments.save()

        return Response(serializer.data)
