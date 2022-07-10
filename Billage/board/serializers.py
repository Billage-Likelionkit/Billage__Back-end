from .models import Board, Board_comments
from rest_framework import serializers


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Board
        fields= '__all__'


##부모는 Board, BoardInfo 
##-> Board 가 호출 됬을 때 Board info 도 함께 출력되도록
##-> Board에  BoardinfoSerialize에 추가

class BoardcommentsSeriallizer(serializers.ModelSerializer):
    # reply = serializers.SerializerMethodField()
    
    class Meta:
        model = Board_comments
        fields = ('id','board_id','content','create_time','writer','comment_id')

    def get_reply(self, instance):
        serializer = self.__class__(instance.reply, many=True)
        serializer.bind('', self)
        return serializer.data

class BoardOnlySerializer(serializers.ModelSerializer):
    parent_comments = serializers.SerializerMethodField()

    class Meta:
        model = Board
        fields = ('id', 'parent_comments')

    def get_parent_comments(self, obj):
        parent_comments = obj.comment.filter(comment_id =None)
        serializer = BoardcommentsSeriallizer(parent_comments, many=True)
        return serializer.data