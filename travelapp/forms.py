from django import forms


# from .models import SignUp

class Signupform(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control p-4', 'placeholder': 'Your name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control p-4', 'placeholder': 'Your email'}))
    # name = forms.CharField()
    # email = forms.EmailField()
    # dest = [SignUp.dest]
