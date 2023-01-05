
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(label='Titre',widget=forms.TextInput(attrs={
        'class':'form-controle',
}))
    content = forms.CharField(label='Content',widget=forms.Textarea(attrs={
    'class':'form-control',
    }))

    class Meta:
        model = Post
        fields = ('title' ,'content', 'image')