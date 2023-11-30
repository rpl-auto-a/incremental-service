from django.db import models
from django.contrib.auth.models import User
from post_properti.models import PostProperti

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
    post = models.ForeignKey(PostProperti, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)