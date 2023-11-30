from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PostProperti(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama_properti = models.CharField(max_length=50)
    deskripsi_properti = models.TextField()
    foto_properti = models.ImageField() 
    kota_properti = models.CharField(max_length=50)
    negara_properti = models.CharField(max_length=50)
    kode_pos_properti = models.CharField(max_length=50)