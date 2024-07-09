from django import forms
from .models import Bookingmodel, SignUpmodel


class Bookingform(forms.ModelForm):
    class Meta:
        model = Bookingmodel
        fields = ['destination', 'duration', 'departDate', 'returnDate']
        widgets = {
            'destination': forms.Select(attrs={
                "style": 'height: 47px',
                "class": 'custom-select px-4 '
            }),
            'duration': forms.Select(attrs={
                "style": 'height: 47px',
                "class": 'custom-select px-4 '
            }),
            'departDate': forms.DateInput(attrs={
                'class': 'form-control p-4 mb-3 datetimepicker-input',
                'type': 'datetime-local',
                "data-target": "#date1",
                "data-toggle": "datetimepicker"
            }),
            'returnDate': forms.DateInput(attrs={
                'class': 'form-control p-4 mb-3',
                'type': 'datetime-local'
            })
        }


class Signupform(forms.Form):
    name = forms.CharField(label=" ", label_suffix=" ",
                           widget=forms.TextInput(attrs={'class': 'form-control p-4 mb-3', 'placeholder': 'Your name'}))
    email = forms.EmailField(label=" ", label_suffix=" ", widget=forms.EmailInput(
        attrs={'class': 'form-control p-4 mb-3', 'placeholder': 'Your email'}))
