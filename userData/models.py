from django.db import models
from django.contrib.auth.models import User
from post_properti.models import PostProperti

# Create your models here.
class UserData (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    nomorWA = models.CharField(max_length=15)
    daftarPost = models.ManyToManyField(PostProperti, blank=True, related_name='daftarPost')
    postFavorit = models.ManyToManyField(PostProperti, blank=True, related_name='postFavorit')