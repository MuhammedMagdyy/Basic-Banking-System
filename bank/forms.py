from queue import Empty
from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    email = forms.CharField(required=True)
    balance = forms.CharField(required=True)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        receiver = Profile.objects.filter(email=email)
        if not len(receiver):
            self.add_error('email', "Email does not exist")

    class Meta:
        model = Profile
        fields = [
            "email",
            "balance"
        ]
