from django.urls import path
from post_properti.views import *

urlpatterns = [
    # other patterns...
    path('', show_all_posts, name='show_all_posts'),
    path('post/<int:id>/', show_post_detail, name='show_post_detail'),
    path('add_post/', add_post, name='add_post'),
    path('edit_post/<int:post_id>/', edit_post, name='edit_post'),
    path('search_post/', search_post_by_name, name='search_post'),
    path('json/', all_posts_json, name='all_posts_json'),
    path('user_posts/', show_user_posts, name='show_user_posts'),
    path('filter_posts/', filter_posts, name='filter_posts'),
]