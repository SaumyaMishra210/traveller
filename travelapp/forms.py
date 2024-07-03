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

        # class Bookingform(forms.Form):
        #     BOOKING_DESTINATION = [
        #         ('', 'Destination'),
        #         ('Destination1', 'Destination1'),
        #         ('Destination2', 'Destination2'),
        #         ('Destination3', 'Destination3'),
        #     ]
        #     destination_type = forms.ChoiceField(choices=BOOKING_DESTINATION, label='',
        #                                          widget=forms.Select(
        #                                              attrs={"style": 'height: 47px', "class": 'custom-select px-4',
        #                                                     'placeholder': 'Select Booking Type'}))
        #     depart_date = forms.DateField(widget=forms.widgets.DateTimeInput(
        #         attrs={'class': 'form-control p-4 mb-3', 'placeholder': 'Depart Date', 'type': 'datetime-local'}))
        #
        #     return_date = forms.DateField(widget=forms.widgets.DateTimeInput(
        #         attrs={'class': 'form-control p-4 mb-3', 'placeholder': 'Return Date', 'type': 'datetime-local'}))
        #
        #     BOOKING_DURATION = [
        #         ('', 'Duration'),
        #         ('Duration1', 'Duration1'),
        #         ('Duration2', 'Duration2'),
        #         ('Duration3', 'Duration3'),
        #     ]
        #     duration_type = forms.ChoiceField(choices=BOOKING_DURATION, label='',
        #                                       widget=forms.Select(
        #                                           attrs={"style": 'height: 47px', "class": 'custom-select px-4',
        #                                                  'placeholder': 'Select Booking Type'}))


class Signupform(forms.Form):
    name = forms.CharField(label=" ", label_suffix=" ",
                           widget=forms.TextInput(attrs={'class': 'form-control p-4 mb-3', 'placeholder': 'Your name'}))
    email = forms.EmailField(label=" ", label_suffix=" ", widget=forms.EmailInput(
        attrs={'class': 'form-control p-4 mb-3', 'placeholder': 'Your email'}))
