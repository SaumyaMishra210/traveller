from django.shortcuts import render, redirect
from .forms import Signupform, Bookingform


# Create your views here.

def about(request):
    return render(request, "about.html")


def index(request):
    if request.method == "POST":
        if 'booking_form' in request.POST:
            booking_form = Bookingform(request.POST)
            if booking_form.is_valid():
                destination = booking_form.cleaned_data['destination']
                duration = booking_form.cleaned_data['duration']
                depart_time = booking_form.cleaned_data['depart_time']
                return_time = booking_form.cleaned_data['return_time']
                return redirect('about')
        else:
            booking_form = Bookingform()
            if 'signup' in request.POST:
                signup_form = Signupform(request.POST)
                if signup_form.is_valid():
                    return redirect('index')
            else:
                signup_form = Signupform()

    else:
        signup_form = Signupform()
        booking_form = Bookingform()

    return render(request, 'index.html', {
        'signup_form': signup_form,
        'booking_form': booking_form
    })


# def bookingformdata(request):
#     booking = Bookingform()
#     return render(request, 'index.html', {"booking": booking})


# def signUpFormData(request):
#     if request.method == 'POST':
#         data = Signupform(request.POST)
#         if data.is_valid():
#             Signupform.objects.create(
#                 name=data.cleaned_data['name'],
#                 email=data.cleaned_data['email']
#             )
#             return redirect('index')
#     else:
#         data = Signupform()
#     return render(request, 'index.html', {"form": data})
