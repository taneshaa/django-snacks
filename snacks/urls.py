from django.urls import path

from .views import HomePageView, AboutView, SnacksView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("snacks", SnacksView.as_view(), name="snacks")
]