from rest_framework import serializers
from .models import Post,Comment,Like
from django.db.models import Count,Max,Min,Avg




 #  Сериализатор    для    комментариев

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields ='__all__'


# Сериализатор для постов с фото
class PostSerializer(serializers.ModelSerializer):
    author=serializers.HiddenField(default=serializers.CurrentUserDefault())
    created_at=serializers.HiddenField(default=serializers.CurrentUserDefault())
    comment=CommentSerializer(many=False,read_only=True,source=('author'))
    likes_count = serializers.SerializerMethodField()

    def get_likes_count(self, obj):
         return Like.objects.filter(post=obj).count()

    class Meta:
        model=Post
        fields=['id','text','author','created_at','image','likes_count','comment']
#Сериализатор для лайков
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
