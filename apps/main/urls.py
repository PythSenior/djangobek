from django.urls import path
from .views import post_list, create_post, delete_post

urlpatterns = [path('', post_list),path('create/',create_post), path('delete/<int:id>/', delete_post)]