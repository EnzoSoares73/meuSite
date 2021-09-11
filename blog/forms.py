from django import forms

from blog.models import Post


class PostForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 20,
            'cols': 200}),
        label='Texto')

    class Meta:
        model = Post
        fields = ('__all__')