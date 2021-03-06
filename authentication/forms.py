from django import forms

from authentication.models import User


class EmailForm(forms.Form):
    emaildummy = 'dummy@dummy.com'
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Nome',
            'class': 'input100'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email',
            'class': 'input100'}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Digite aqui a sua mensagem',
            'style': 'wrap: hard; height: 90px',
            'class': 'input100'}), max_length=500)
    email_dummy = forms.EmailField(
        widget=forms.HiddenInput(attrs={
            'value': emaildummy,
            'required': '',
        }))

class UserForm(forms.ModelForm):
    ddd = forms.CharField(widget=forms.TextInput(attrs={
            'style': 'widht: 90'})
    )
    class Meta:
        model = User
        fields = ('__all__')

