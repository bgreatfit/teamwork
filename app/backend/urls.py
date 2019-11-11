from django.urls import path
from .views import GifCreateAPIView, ArticleCreateAPIView

# from .views import Registe
#
urlpatterns = [
     path('gifs', GifCreateAPIView.as_view(), name="gif-create"),
     path('articles', ArticleCreateAPIView.as_view(), name="article-create"),
]