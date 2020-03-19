from django import forms


class Auth(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='password')

