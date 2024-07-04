from django.shortcuts import render, redirect
from .models import Bookingmodel, SignUpmodel


# Create your views here.
def index(request):
    if request.method == 'POST':
        if 'booking_form' in request.POST:
            destination = request.POST.get('destination')
            duration = request.POST.get('duration')
            departDate = request.POST.get('departDate')
            returnDate = request.POST.get('returnDate')

            # Create and save BookingModel instance
            booking_instance = Bookingmodel(
                destination=destination,
                duration=duration,
                departDate=departDate,
                returnDate=returnDate,
            )
            # breakpoint()
            booking_instance.save()

        elif 'user_form' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            dest = request.POST.get('destination')

            user_profile = SignUpmodel(name=name, email=email,destination=dest)
            user_profile.save()

        return redirect('success')

    else:
        print("else part")
    booking_instance = Bookingmodel()
    user_profile = SignUpmodel()
    return render(request, 'index.html', {'bookings': booking_instance,'user_profile':user_profile})


# def formView(request):
#     if request.method == 'POST':
#         print('inside post')
#         destination = request.POST.get('destination')
#         duration = request.POST.get('duration')
#         departDate = request.POST.get('departDate')
#         returnDate = request.POST.get('returnDate')
#
#         bookings = Bookingmodel(destination=destination, duration=duration, departDate=departDate,
#                                 returnDate=returnDate)
#         bookings.save()
#         return redirect('success')
#     bookings = Bookingmodel()
#     return render(request, 'formpage.html', {'bookings': bookings})


def success(request):
    return render(request, 'success.html')


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


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

def book_details1(request):
    bookings = Bookingmodel.objects.all()
    return render(request, 'NEW.html', {'bookings': bookings})
