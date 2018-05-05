from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView),
    path('about/', views.AboutListView),
    path('resume/', views.ResumeView.as_view()),
]
