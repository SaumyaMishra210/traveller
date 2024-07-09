from django.shortcuts import render, redirect
from .models import Bookingmodel, SignUpmodel
from django.contrib import messages


# Create your views here.
def about(request):
    return render(request, "about.html")

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request, "contact.html")

def destination(request):
    return render(request,'destination.html')

def guide(request):
    return render(request,'guide.html')

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
            password = request.POST.get('password')
            rpassword = request.POST.get('rpassword')
            # dest = request.POST.get('destination')

            if password != rpassword:
                error_message = "Password not matched."
                return render(request, 'index.html', {'error_message': error_message})

            if SignUpmodel.objects.filter(email=email).exists():
                error_message = "Email exists already."
                return render(request, 'index.html', {'error_message': error_message})
            messages.warning(request, 'This is a warning message.')

            user_profile = SignUpmodel(name=name, email=email, password=password, rpassword=rpassword)
            user_profile.save()

        return redirect('success')

    booking_instance = Bookingmodel()
    user_profile = SignUpmodel()
    return render(request, 'index.html', {'bookings': booking_instance, 'user_profile': user_profile})

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def package(request):
    return render(request, 'package.html')

def service(request):
    return render(request, 'service.html')

def single(request):
    return render(request,'single.html')

def success(request):
    return render(request,'success.html')

def testimonial(request):
    return render(request,'testimonial.html')

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
