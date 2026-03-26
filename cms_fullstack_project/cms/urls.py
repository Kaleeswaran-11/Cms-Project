from django.urls import path
from . import views
urlpatterns=[
 path('',views.home,name='home'),
 path('register/',views.register,name='register'),
 path('dashboard/',views.dashboard,name='dashboard'),
 path('post/create/',views.create_post,name='create_post'),
 path('post/edit/<int:pk>/',views.update_post,name='update_post'),
 path('post/delete/<int:pk>/',views.delete_post,name='delete_post'),
 path('post/<int:pk>/',views.post_detail,name='post_detail'),
 path('profile/',views.profile,name='profile'),
]
