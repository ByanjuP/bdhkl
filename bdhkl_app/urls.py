from django.contrib import admin
from django.urls import path
from . import views
from .views import post_create,destination_create
from .views import PostListView,PostDetailView


urlpatterns = [
    path('', views.home, name='home'),
    path('postcreate/',views.post_create,name = 'post-create'),
    path('destinationscreate/',views.destination_create,name = 'destination-create'),
    path('postlist/',PostListView.as_view(),name = 'post-list'),
    path('postdetail/<int:pk>/', PostDetailView.as_view(), name='post-detail'),






]
