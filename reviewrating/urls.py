from django.urls import path
from reviewrating.views import *

app_name = 'review'

urlpatterns = [
    path("", show_reviews, name="show_reviews"),
    path("add/", add_review, name="add_review"),
    path("edit/<int:id>", edit_review, name="edit_review"),
]