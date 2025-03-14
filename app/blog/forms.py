from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 20,
            'cols': 100}),
        label='Texto')

    class Meta:
        model = Post
        fields = ('__all__')