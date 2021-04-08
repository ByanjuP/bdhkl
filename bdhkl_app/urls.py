from django.contrib import admin
from django.urls import path
from . import views
from .views import post_create,destination_create
from .views import (
    PostListView,PostDetailView,PostDeleteView,PostUpdateView,
    PostCreateView, gallerycreate,hotels,AboutView,ContactView,test_form,del_testform,update_form,DestinationList,DestinationDetail,thingstodo_create,)
from .forms import  UserLoginForm
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name = 'login.html',authentication_form = UserLoginForm),name = 'login'),
    path('accounts/profile/',views.profile, name = 'profile'),
    path('newpost/',views.post_create,name = 'new-post'),
    path('destinationscreate/',views.destination_create,name = 'destination-create'),
    path('thingstodocreate/', views.thingstodo_create, name='thingstodo-create'),
    path('postcreate/',PostCreateView.as_view(),name = 'post-create'),
    path('postlist/',PostListView.as_view(),name = 'post-list'),
    path('postdetail/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('postdelete/<int:pk>/',PostDeleteView.as_view(),name = 'post-delete'),
    path('postupdate/<int:pk>/',PostUpdateView.as_view(),name = 'post-update'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('addgallery/', views.gallerycreate, name = 'gallery-add'),
    path('gallery/',views.gallery, name = 'gallery'),
    path('hotels/',views.hotels, name = 'hotels'),
    path('about/',AboutView.as_view(),name = 'about'),
    path('contact/',ContactView.as_view(),name = 'contact'),
    path('testform/',views.test_form,name ='testform'),
    path('testform/delete/<int:id>/',views.del_testform,name = 'testform-delete'),
    path('testform/update/<int:id>/',views.update_form,name = 'testform-update'),
    path('destinations/',DestinationList.as_view(),name = 'destinations'),
    path('destinations/detail/<int:pk>/',DestinationDetail.as_view(),name = 'destinations-detail'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name = 'password-reset.html'),name = 'password-reset')
    ]
