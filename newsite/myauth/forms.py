from django.contrib.auth.models import User
from django import forms
from .models import Profile
from django.forms.widgets import ClearableFileInput


class EditUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class AddAvatarForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = 'user_avatar',


# TODO: The created_at now returns the UTC time, need to differentiate with the user's local timezone and show correct time (created_at + 4 hours +GMT4)
# TODO: Check if the email is already in use while registration