from django.urls import path
from userData.views import *

app_name = 'userData'

urlpatterns = [
    path ('add/<int:post_id>/', add_favorite, name='add_favorite'),
    path ('delete/<int:id>/', delete_favorite, name='delete_favorite'),
    path ('get/', favorites_json, name='favorites_json'),
    path ('favorite/', favorite, name='favorite'),
]