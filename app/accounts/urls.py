from django.urls import path, include

from knox import views as knox_views
from .views import RegisterAPI, LoginAPI, UserAPI
app_name ="accounts"

urlpatterns = [
  #...snip...
  path('', include('knox.urls')),
  path('create-user', RegisterAPI.as_view(), name='create-user'),
  path('login', LoginAPI.as_view(), name='login'),
  path('user', UserAPI.as_view()),
  path('logout', knox_views.LogoutView.as_view(), name='knox_logout'),
  #...snip...
]