from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={
        'class':'form-controle',
}))
    
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={
        'class':'form-controle',
}))
    
    
    
class UserForm(UserCreationForm):
        username = forms.CharField(label='Username',widget=forms.TextInput(attrs={
        'class':'form-controle',
}))
    
        email = forms.CharField(label='Email',widget=forms.EmailInput(attrs={
    'class':'form-control',
}))
    
        password1 = forms.CharField(label='Password1',widget=forms.PasswordInput(attrs={
        'class':'form-controle',
}))
        password2 = forms.CharField(label='Confirm your password',widget=forms.PasswordInput(attrs={
    'class':'form-control',
    }))

        class Meta:
            model = User
            fields = ('username', 'email', 'password1', 'password2')