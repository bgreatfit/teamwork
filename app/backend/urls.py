from django.urls import path
from .views import GifCreateAPIView, ArticleRetrieveUpdateDestroyAPIView, ArticleListCreateAPIView

# from .views import Registe
#
urlpatterns = [
     path('gifs', GifCreateAPIView.as_view(), name="gif-list"),
     path('articles', ArticleListCreateAPIView.as_view(), name="article-list"),
     path('articles/<int:pk>', ArticleRetrieveUpdateDestroyAPIView.as_view(), name="article-detail"),
]