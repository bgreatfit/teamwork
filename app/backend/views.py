from django.shortcuts import render, get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response
import cloudinary.uploader

from .permissions import IsOwner
from .serializers import GIFSerializer, ArticleSerializer, CommentSerializer, CategorySerializer
from .models import Article, GIF, Comment, Category


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
        queryset = Article.objects.all()
        category_id = self.request.query_params.get('category_id')
        if category_id is not None:
            queryset = Article.objects.filter(category_id=category_id)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

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
    permission_classes = (permissions.IsAuthenticated, IsOwner)

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


class ArticleCommentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        article = Article.objects.get(pk=self.kwargs.get('article_id'))
        return article.comments.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        article = get_object_or_404(
            Article, pk=kwargs.get('article_id')
        )
        if serializer.is_valid() and article:
            comment = serializer.save(owner=self.request.user, article=article)
            return Response({
                "status": "success",
                "data": {
                    "commentId": comment.id,
                    "message": "Comment successfully posted",
                    "createdOn": comment.created_at,
                    "comment": comment.comment,
                    "articleTitle": article.title,
                    "article": article.article,
                }

            }, status=status.HTTP_201_CREATED)
        return Response({
            "status": "error",
            "error": serializer.errors

        }, status=status.HTTP_400_BAD_REQUEST)


class ArticleCommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def get_queryset(self):
        queryset = Comment.objects.filter(article_id=self.kwargs.get('pk'))
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


class GifCommentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.gif.comments.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        gif = get_object_or_404(
            GIF, pk=kwargs.get('gif_id')
        )
        if serializer.is_valid() and gif:
            comment = serializer.save(owner=self.request.user, gif=gif)
            return Response({
                "status": "success",
                "data": {
                    "commentId": comment.id,
                    "message": "Comment successfully posted",
                    "createdOn": comment.created_at,
                    "comment": comment.comment,
                }

            }, status=status.HTTP_201_CREATED)
        return Response({
            "status": "error",
            "error": serializer.errors

        }, status=status.HTTP_400_BAD_REQUEST)


class GifCommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def get_queryset(self):
        queryset = Comment.objects.filter(article_id=self.kwargs.get('pk'))
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


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
