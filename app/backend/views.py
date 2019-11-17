from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response
import cloudinary.uploader

from . permissions import IsOwner
from .serializers import GIFSerializer, ArticleSerializer
from .models import Article, GIF


# Create your views here.


class GifCreateAPIView(generics.CreateAPIView):
    serializer_class = GIFSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (
        MultiPartParser,
        JSONParser,
    )

    def get_queryset(self):
        return self.request.user.gifs.all()

    def post(self, request, *args, **kwargs):
        file = request.data.get('image')
        upload_data = cloudinary.uploader.upload(file)
        request.data.pop('image')
        request.data['image_url'] = upload_data['secure_url']
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid() and upload_data:
            gif = serializer.save(owner=self.request.user)
            return Response({
                "status": "success",
                "data": {
                    "gifId": gif.id,
                    "message": "image successfully posted",
                    "createdOn": gif.created_at,
                    "title": gif.title,
                    "imageUrl": upload_data['secure_url'],
                }

            }, status=status.HTTP_201_CREATED)
        return Response({
            "status": "error",
            "error": serializer.errors

        }, status=status.HTTP_400_BAD_REQUEST)


class GifRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GIFSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def get_queryset(self):
        queryset = GIF.objects.filter(pk=self.kwargs.get('pk'))
        return queryset

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(instance=self.get_object())
        if serializer.data:
            return Response({
                "status": "success",
                "data": {
                    "articleId": serializer.data['id'],
                    "article": serializer.data['article'],
                    "title": serializer.data['title'],
                }

            }, status=status.HTTP_200_OK)
        return Response({
            "status": "error",
            "error": serializer.errors

        }, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, partial=True, instance=self.get_object())
        if serializer.is_valid():
            article = serializer.save(owner=self.request.user)
            return Response({
                "status": "success",
                "data": {
                    "articleId": article.id,
                    "message": "Article successfully updated",
                    "createdOn": article.created_at,
                    "title": article.title,
                    "article": article.article,
                }

            }, status=status.HTTP_201_CREATED)
        return Response({
            "status": "error",
            "error": serializer.errors

        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            self.perform_destroy(instance)
            return Response({
                "status": "success",
                "data": {
                    "message": "gif successfully deleted",
                }

            }, status=status.HTTP_204_NO_CONTENT)
        return Response({
            "status": "error",
            "error": "Article cannot be found"

        }, status=status.HTTP_400_BAD_REQUEST)


class ArticleListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.articles.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            article = serializer.save(owner=self.request.user)
            return Response({
                "status": "success",
                "data": {
                    "articleId": article.id,
                    "message": "Article successfully posted",
                    "createdOn": article.created_at,
                    "title": article.title,
                    "article": article.article,
                }

            }, status=status.HTTP_201_CREATED)
        return Response({
            "status": "error",
            "error": serializer.errors

        }, status=status.HTTP_400_BAD_REQUEST)


class ArticleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner )

    def get_queryset(self):
        queryset = Article.objects.filter(pk=self.kwargs.get('pk'))
        return queryset

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(instance=self.get_object())
        if serializer.data:
            return Response({
                "status": "success",
                "data": {
                    "articleId": serializer.data['id'],
                    "article": serializer.data['article'],
                    "title": serializer.data['title'],
                }

            }, status=status.HTTP_200_OK)
        return Response({
            "status": "error",
            "error": serializer.errors

        }, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, partial=True, instance=self.get_object())
        if serializer.is_valid():
            article = serializer.save(owner=self.request.user)
            return Response({
                "status": "success",
                "data": {
                    "articleId": article.id,
                    "message": "Article successfully updated",
                    "createdOn": article.created_at,
                    "title": article.title,
                    "article": article.article,
                }

            }, status=status.HTTP_201_CREATED)
        return Response({
            "status": "error",
            "error": serializer.errors

        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            self.perform_destroy(instance)
            return Response({
                "status": "success",
                "data": {
                    "message": "Article successfully deleted",
                }

            }, status=status.HTTP_204_NO_CONTENT)
        return Response({
            "status": "error",
            "error": "Article cannot be found"

        }, status=status.HTTP_400_BAD_REQUEST)
