from django import forms
from models import Profile
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo','name','bio')


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'photo', 'bio']