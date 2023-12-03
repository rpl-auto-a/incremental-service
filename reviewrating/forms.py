from django import forms
from reviewrating.models import Review

class ReviewForm(forms.ModelForm):
    CHOICES = [
        ('1', int(1)),
        ('2', int(2)),
        ('3', int(3)),
        ('4', int(4)),
        ('5', int(5)),
    ]
    class Meta:
        model = Review
        fields = ['rating', 'review']
