from django.urls import path
from post_properti.views import *

urlpatterns = [
    # other patterns...
    path('edit_post/<int:post_id>/', edit_post, name='edit_post'),
    path('search_post/', search_post_by_name, name='search_post'),
]