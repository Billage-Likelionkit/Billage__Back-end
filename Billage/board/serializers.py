from .models import Board, Board_comments
from rest_framework import serializers


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Board
        fields= '__all__'


##부모는 Board, BoardInfo 
##-> Board 가 호출 됬을 때 Board info 도 함께 출력되도록
##-> Board에  BoardinfoSerialize에 추가

class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, instance):
        serializer = self.comment_id.__class__(instance, context=self.context)
        return serializer.data

class BoardcommentsSeriallizer(serializers.ModelSerializer):
    reply = serializers.SerializerMethodField()
    board_id = serializers.SlugRelatedField(queryset=Board.objects.all(), slug_field='id')
    
    class Meta:
        model = Board_comments
        fields = '__all__'

    def get_reply(self, instance):
        serializer = self.__class__(instance.reply, many=True)
        serializer.bind('', self)
        return serializer.data