from django.urls import path

from blogapp import views

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
]
