from django.urls import include, path
from post_properti.views import *

urlpatterns = [
    # other patterns...
    path('', show_all_posts, name='show_all_posts'),
    path('<int:id>/', show_post_detail, name='show_post_detail'),
    path('new/', new_post, name='new_post'),
    path('<int:id>/reviews/', include('reviewrating.urls')),
    path('add_post/', add_post, name='add_post'),
    path('edit_post/<int:id>/', edit_post, name='edit_post'),
    path('search_post/', search_post_by_name, name='search_post'),
    path('json/', all_posts_json, name='all_posts_json'),
    path('user_posts/', show_user_posts, name='show_user_posts'),
    path('user_posts_json/', user_posts_json, name='user_posts_json'),
    path('filter_posts/', filter_posts, name='filter_posts'),
    path('get_kota_choices/', get_kota_choices, name='get_kota_choices'),
]