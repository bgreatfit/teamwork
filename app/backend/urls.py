from django.urls import path
from .views import GifCreateAPIView, ArticleRetrieveUpdateDestroyAPIView, ArticleListCreateAPIView, \
     GifRetrieveUpdateDelete

# from .views import Registe
#
print()
urlpatterns = [
     path('gifs', GifCreateAPIView.as_view(), name="gif-list"),
     path('gifs/<int:pk>', GifRetrieveUpdateDelete.as_view(), name="gif-detail"),
     path('articles', ArticleListCreateAPIView.as_view(), name="article-list"),
     path('articles/<int:pk>', ArticleRetrieveUpdateDestroyAPIView.as_view(), name="article-detail"),
]