from .models import Board
from rest_framework import serializers


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Board
        fields= '__all__'



##부모는 Board, BoardInfo 
##-> Board 가 호출 됬을 때 Board info 도 함께 출력되도록
##-> Board에  BoardinfoSerialize에 추가