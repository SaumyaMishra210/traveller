from django import forms

class Bookingform(forms.Form):
    BOOKING_DESTINATION = [
        ('', 'Destination'),
        ('Destination1','Destination1'),
        ('Destination2','Destination2'),
        ('Destination3','Destination3'),
    ]
    destination_type = forms.ChoiceField(choices=BOOKING_DESTINATION, label='',
                                     widget=forms.Select(attrs={"style":'height: 47px',"class":'custom-select px-4','placeholder': 'Select Booking Type'}))
    depart_date = forms.CharField(label=" ",label_suffix=" ", widget=forms.TextInput(attrs={'class': 'form-control p-4 mb-3', 'placeholder': 'Depart Date'}))

    return_date = forms.CharField(label=" ",label_suffix=" ",widget=forms.TextInput(attrs={'class': 'form-control p-4 mb-3', 'placeholder': 'Return Date'}))

    BOOKING_DURATION = [
        ('', 'Duration'),
        ('Duration1', 'Duration1'),
        ('Duration2', 'Duration2'),
        ('Duration3', 'Duration3'),
    ]
    duration_type = forms.ChoiceField(choices=BOOKING_DURATION, label='',
                                         widget=forms.Select(
                                             attrs={"style": 'height: 47px', "class": 'custom-select px-4',
                                                    'placeholder': 'Select Booking Type'}))

class Signupform(forms.Form):
    name = forms.CharField(label=" ",label_suffix=" ",widget=forms.TextInput(attrs={'class': 'form-control p-4 mb-3', 'placeholder': 'Your name'}))
    email = forms.EmailField(label=" ",label_suffix=" ",widget=forms.EmailInput(attrs={'class': 'form-control p-4 mb-3', 'placeholder': 'Your email'}))
    # dest = [SignUp.dest]
