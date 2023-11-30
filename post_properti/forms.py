from django import forms
from .models import PostProperti

class PostPropertiForm(forms.ModelForm):
    class Meta:
        model = PostProperti
        fields = ['nama_properti', 'deskripsi_properti', 'foto_properti', 'kota_properti', 'negara_properti', 'kode_pos_properti']
