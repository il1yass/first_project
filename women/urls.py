from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/',about, name='about'),
    path('addpage/',addpage, name='addpage'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/',RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/,', show_post, name='post'),
    path('category/<slug:cat_slug>/,', show_category, name='category'),
    path('logout/', logout_user, name='logout'),
]

