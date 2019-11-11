from django.urls import path
from . views import GifCreateAPIView
# from .views import Registe
#
urlpatterns = [
     path('gifs', GifCreateAPIView.as_view(), name="gif-create"),
]