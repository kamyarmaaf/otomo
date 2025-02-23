from django.urls import path
from . import views
from .views import AllKhabarsView, AllReviewView

urlpatterns = [
    path("", views.home, name="home"),
    path("reviews/<slug:slug>/", views.SingleReviewView.as_view(), name="reviews"),
    path("akhbar/<slug:slug>/", views.SingleKhabarView.as_view(), name="khabars"),
    path("allposts/akhbar/", AllKhabarsView.as_view(), name="all_khabars"),
    path("allposts/reviews/", AllReviewView.as_view(), name="all_review"),
    path("search/", views.search, name="search"),
    path("about/", views.about, name="about"),
]
