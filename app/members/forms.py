from django import forms


class SignupForm(forms.Form):
    username = forms.CharField(label ='username')
    email = forms.EmailField(label ='email')
    password = forms.CharField(
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput()
    )

    pass