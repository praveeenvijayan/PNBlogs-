from django.urls import path
from .views import  blog, blog_details, add_blog, update_blog, delete_post

urlpatterns = [
    # path('', views.blog, name="blog"),
    path('', blog.as_view(), name="blog"),
    path('post/<int:pk>', blog_details.as_view(), name="blog-details"),
    path('add_blog/', add_blog.as_view(), name="add-post"),
    path('edit_blog/<int:pk>', update_blog.as_view(), name="edit-post"),
    path('post/<int:pk>/delete', delete_post.as_view(), name="delete-post"),
]