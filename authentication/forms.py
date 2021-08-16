from django import forms

class EmailForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Name',
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