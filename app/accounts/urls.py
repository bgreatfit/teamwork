from django.conf.urls import include, url
from knox import views as knox_views
from .api import RegisterAPI, LoginAPI, UserAPI

urlpatterns = [
  #...snip...
  url(r'', include('knox.urls')),
  url(r'register', RegisterAPI.as_view()),
  url(r'login', LoginAPI.as_view()),
  url(r'user', UserAPI.as_view()),
  url(r'logout', knox_views.LogoutView.as_view(), name='knox_logout'),
  #...snip...
]