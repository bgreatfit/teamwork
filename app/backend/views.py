import cloudinary as cloudinary
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response
import cloudinary.uploader

from .serializers import GIFSerializer


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
        print(file)

        upload_data = cloudinary.uploader.upload(file)
        request.data.pop('image')
        request.data['image_url'] = upload_data['secure_url']
        serializer = self.get_serializer(data=request.data)

        print(upload_data)
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
