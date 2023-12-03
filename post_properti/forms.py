from django import forms
from .models import PostProperti

class PostPropertiForm(forms.ModelForm):
    class Meta:
        model = PostProperti
        fields = ['nama_properti', 'deskripsi_properti', 'foto_properti', 'negara_properti', 'kota_properti', 'kode_pos_properti']

class FilterForm(forms.Form):
    negara = forms.ChoiceField(label='Negara', choices=[])
    kota = forms.ChoiceField(label='Kota', choices=[], required=False)

    def __init__(self, *args, **kwargs):
        super(FilterForm, self).__init__(*args, **kwargs)
        self.fields['kota'].widget.attrs['disabled'] = 'disabled'

    def set_kota_choices(self, kota_choices):
        self.fields['kota'].choices = kota_choices