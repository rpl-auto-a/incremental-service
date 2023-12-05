from django.contrib.auth.forms import UserCreationForm
from django import forms
from userData.models import UserData
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    name = forms.CharField(required=True)
    nomorWA = forms.RegexField(regex=r'^\+?1?\d{9,15}$', 
                               error_messages = {"invalid": "Phone number must be entered in the format: '+628123456789'."})

    class Meta:
        model = User
        fields = ("username", "name", "nomorWA", "password1", "password2")

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)

        if commit:
            user.save()

        print("test")
        UserData.objects.create(
            user = user,
            name = self.cleaned_data["name"],
            nomorWA = self.cleaned_data["nomorWA"],
        )
        return user