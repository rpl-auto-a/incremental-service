from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)