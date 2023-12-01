from django.db import models
from django.contrib.auth.models import User
from post_properti.models import PostProperti

# Create your models here.
class UserData (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    nomorWA = models.CharField(max_length=15)
    daftarPost = models.ManyToManyField(PostProperti, blank=True)
    postFavorit = models.ManyToManyField(PostProperti, blank=True, related_name='postFavorit')
