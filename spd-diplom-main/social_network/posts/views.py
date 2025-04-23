from rest_framework.decorators import api_view, permission_classes
from .models import Post,Comment,Like
from .serializers import PostSerializer,CommentSerializer,LikeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (IsAuthenticated, IsAdminUser, SAFE_METHODS)
from rest_framework.permissions import   (IsAuthenticatedOrReadOnly)
from .permissions import (AuthorOrReadOnly,IsOwnerOrReadOnly)
from rest_framework import generics



class PostListCreateView(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer=PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]


class CommentListCreateView(generics.ListCreateAPIView):
     queryset=Comment.objects.all()
     serializer = CommentSerializer(queryset,many=True)
     permission_classes = [IsAuthenticatedOrReadOnly]
     def perform_create(self, serializer):
         serializer.save(user=self.request.user)

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]



class LikeView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request, *arqs, **kwargs):
        likes = Like.objects.all()
        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data)
        

    def post(self, request, *arqs, **kwargs):
        post_id=request.data.get("post")
        post = Post.objects.get(id=post_id)
        queryset = Like.objects.all()
        like,created = Like.objects.get_or_create(user=request.user,post=post)
        if not created:
            like.delete()
            return Response({"message":"Like removed"},status=204)
        return Response({"message":"Liked"},status=201)


