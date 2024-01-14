from django.urls import path

from video_player import views

urlpatterns = [
    path("", views.home, name="home"),
]
