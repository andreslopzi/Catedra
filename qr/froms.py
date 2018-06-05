from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminSplitDateTime
from django.contrib.auth.models import User

from .models import *
from django.core.validators import RegexValidator



class UserForm(forms.ModelForm):
    password = forms.CharField(label='Contrasena', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirmar contrasena',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password:
            if len(password) < 6:
                raise forms.ValidationError("La contrasena debe tener una longitud minima de 6 caracteres")
        if not password2:
            raise forms.ValidationError("Debe confirmar la contrasena")
        if password != password2:
            raise forms.ValidationError("Las contrasenas no coinciden")
        return password2

    class Meta:
        model = User
        fields = ['password']