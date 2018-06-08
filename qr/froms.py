from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminSplitDateTime
from django.contrib.auth.models import User

from .models import *
from django.core.validators import RegexValidator


username_validator = RegexValidator(r'^[0-9a-z]*$',
                                    "Solo letras y numeros (sin espacios ni mayusculas)")

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


class CreateUserForm(forms.ModelForm):
    username = forms.CharField(validators=[username_validator], max_length=20,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirmar contraseña',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password:
            if len(password) < 6:
                raise forms.ValidationError("La contraseña debe tener una longitud minima de 6 caracteres")
        if not password2:
            raise forms.ValidationError("Debe confirmar la contraseña")
        if password != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    class Meta:
        model = User
        fields = ['username', 'email', 'password']