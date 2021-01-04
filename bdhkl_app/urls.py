from django.contrib import admin
from django.urls import path
from . import views
from .views import post_create,destination_create
from .views import PostListView,PostDetailView,PostDeleteView,PostUpdateView,PostCreateView, gallerycreate


urlpatterns = [
    path('', views.home, name='home'),
    path('newpost/',views.post_create,name = 'new-post'),
    path('destinationscreate/',views.destination_create,name = 'destination-create'),
    path('postcreate/',PostCreateView.as_view(),name = 'post-create'),
    path('postlist/',PostListView.as_view(),name = 'post-list'),
    path('postdetail/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('postdelete/<int:pk>/',PostDeleteView.as_view(),name = 'post-delete'),
    path('postupdate/<int:pk>/',PostUpdateView.as_view(),name = 'post-update'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('addgallery/', views.gallerycreate, name = 'gallery-add'),
    path('gallery/',views.gallery, name = 'gallery')
]
