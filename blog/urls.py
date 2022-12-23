from django.urls import path
from blog.views import *
urlpatterns = [
    path('posts/add', add_post),
    path('posts/', view_posts)
]
