from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name="main-page"),
    path('posts/', views.posts, name="posts"),
    path('posts/categories/', views.post_categories, name="posts-categories"),
    path('post/categories/<str:category>', views.show_category_content, name="post-category"),
    path('posts/<str:post_title>/', views.get_post_content, name="blog-posts"),
]
