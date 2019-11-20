from django.urls import path
from .views import GifCreateAPIView, ArticleRetrieveUpdateDestroyAPIView, ArticleListCreateAPIView, \
     GifRetrieveUpdateDelete, ArticleCommentListCreateAPIView, GifCommentListCreateAPIView, CategoryListCreateAPIView, \
     FlagCreateAPIView

# from .views import Registe
#
print()
urlpatterns = [
     path('gifs', GifCreateAPIView.as_view(), name="gif-list"),
     path('gifs/<int:pk>', GifRetrieveUpdateDelete.as_view(), name="gif-detail"),
     path('gifs/<int:pk>', GifRetrieveUpdateDelete.as_view(), name="gif-detail"),
     path('gifs/<int:gif_id>/comment', GifCommentListCreateAPIView.as_view(), name="comment-list-gif"),
     path('articles', ArticleListCreateAPIView.as_view(), name="article-list"),
     path('articles/<int:pk>', ArticleRetrieveUpdateDestroyAPIView.as_view(), name="article-detail"),
     path('articles/<int:article_id>/comment', ArticleCommentListCreateAPIView.as_view(), name="comment-list-article"),
     path('articles/<int:article_id>/flag', FlagCreateAPIView.as_view(), name="flag-article"),
     path('gifs/<int:gif_id>/flag', FlagCreateAPIView.as_view(), name="flag-gif"),
     path('comments/<int:comment_id>/flag', FlagCreateAPIView.as_view(), name="flag-comment"),
     path('categories', CategoryListCreateAPIView.as_view(), name="category-list"),
]