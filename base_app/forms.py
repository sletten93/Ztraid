# from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ZtrUser


class ZtrUserCreationForm(UserCreationForm):

    class Meta:
        model = ZtrUser
        fields = ('username', 'email')


class ZtrUserChangeForm(UserChangeForm):

    class Meta:
        model = ZtrUser
        fields = UserChangeForm.Meta.fields
