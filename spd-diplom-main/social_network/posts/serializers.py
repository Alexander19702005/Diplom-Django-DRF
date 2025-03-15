from rest_framework import serializers
from .models import Post
from .models import Post_1
from .models import Like
from django.db.models import Count,Max,Min,Avg




 #  Сериализатор    для    комментариев

class Post_1Serializer(serializers.ModelSerializer):

    class Meta:
        model = Post_1
        fields ='__all__'


# Сериализатор для постов с фото
class PostSerializer(serializers.ModelSerializer):
    author=serializers.HiddenField(default=serializers.CurrentUserDefault())
    comment=Post_1Serializer(many=False,read_only=True,source=('author'))
    likes_count = serializers.SerializerMethodField()

    def get_likes_count(self, obj):
        return Like.objects.aggregate(likes_count=Count('like'))

    class Meta:
        model=Post
        fields=['id','text','author','created_at','image','comment','likes_count']
#Сериализатор для лайков
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
