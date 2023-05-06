from django.urls import path
from . import views
  
urlpatterns = [
    path("", views.home, name="home"),
    path("all/", views.all, name="all"),
    path("chineses/", views.chineses, name="chineses"),
    path("french/", views.french, name="french"),
    path("german/", views.german, name="german"),
    path("italian/", views.italian, name="italian"),
    path("japanese/", views.japanese, name="japanese"),
    path("korean/", views.korean, name="korean"),
    path("spanish/", views.spanish, name="spanish"),
]

