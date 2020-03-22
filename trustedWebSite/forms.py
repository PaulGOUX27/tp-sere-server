from django import forms


class Auth(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='password', widget=forms.PasswordInput)


class Add(forms.Form):
    username = forms.CharField(label='username')
    comment = forms.CharField(widget=forms.Textarea)
