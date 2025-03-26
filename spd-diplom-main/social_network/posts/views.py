from rest_framework.decorators import api_view, permission_classes
from .models import Post
from .models import Post_1
from .models import Like
from .serializers import LikeSerializer
from .serializers import PostSerializer
from .serializers import Post_1Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (IsAuthenticated, IsAdminUser, SAFE_METHODS)
from rest_framework.permissions import   (IsAuthenticatedOrReadOnly)
from .permissions import (IsOwnerOrReadOnly)
from rest_framework import generics


class PostView(APIView):
    permission_classes=(IsAuthenticated)
    def get(self,request, *arqs , **kwargs):
        queryset=Post.objects.all()
        serializer=PostSerializer(queryset,many=True)
        return Response(serializer.data)

    permission_classes=(IsAuthenticated)
    def post(self,request,*args,**kwargs):
        queryset = Post.objects.all()
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    permission_classes = ([IsOwnerOrReadOnly])
    def patch(self,request,*args,**kwargs):        
        queryset = Post.objects.all()
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    permission_classes = ([IsOwnerOrReadOnly])
    def delete(self,request,*args,**kwargs):       

        queryset = Post.objects.all()
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class Post_1View(APIView):
    permission_classes=(IsAuthenticated)
    def get(self,request, *arqs , **kwargs):
        queryset=Post_1.objects.all()
        serializer=Post_1Serializer(queryset,many=True)
        return Response(serializer.data)
        
    permission_classes=(IsAuthenticated) 
    def post(self,request, *arqs , **kwargs):
        queryset = Post_1.objects.all()
        serializer = Post_1Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
        
    permission_classes=([IsOwnerOrReadOnly])
    def patch(self,request, *arqs , **kwargs):
        queryset = Post_1.objects.all()
        serializer = Post_1Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class LikeView(APIView):
    permission_classes=(IsAuthenticated)
    def get(self, request, *arqs, **kwargs):
        queryset = Like.objects.all()
        serializer = LikeSerializer(queryset, many=True)
        return Response(serializer.data)
    permission_classes=(IsAuthenticated)
    def post(self, request, *arqs, **kwargs):
        queryset = Like.objects.all()
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)



