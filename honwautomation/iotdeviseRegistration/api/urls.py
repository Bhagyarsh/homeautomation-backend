# api/urls.py
from django.urls import include, path
from .views import RegisterAPIView
urlpatterns = [

#    path('auth/jwt', AuthAPIView.as_view()),
    path('register/device', RegisterAPIView.as_view()),

]
