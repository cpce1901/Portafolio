from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Usuario',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'Usuario',
                'id' : 'floatingInput',
                'class' : 'form-control px-5',
            }
        ) 
    )

    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Contraseña',
                'id' : 'floatingPassword',
                'class' : 'form-control',
            }
        ) 
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Los datos de usuario no son correctos')

        return self.cleaned_data

        
class UpassForm(forms.Form):
    password1 = forms.CharField(
        label='Contraseña Actual',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Contraseña Actual',
                'id' : 'floatingPassword',
                'class' : 'form-control',
            }
        ) 
    )

    password2 = forms.CharField(
        label='Nueva Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Nueva Contraseña',
                'id' : 'floatingPassword',
                'class' : 'form-control',
            }
        ) 
    )