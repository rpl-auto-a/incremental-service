from django.urls import path
from reviewrating.views import *

urlpatterns = [
    path("add/<int:book_id>/", add_review, name="add_review"),
    path("all/<int:book_id>/", reviews_json, name="reviews_json"),
    path("delete/<int:id>", delete_review, name="delete_review"),
]