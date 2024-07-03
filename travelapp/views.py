from django.shortcuts import render, redirect
from .models import Bookingmodel


# Create your views here.
def index(request):
    if request.method == 'POST':
        destination = request.POST.get('destination')
        duration = request.POST.get('duration')
        departDate = request.POST.get('departDate')
        returnDate = request.POST.get('returnDate')

        # Create and save BookingModel instance
        booking_instance = Bookingmodel(
            destination=destination,
            duration=duration,
            departDate = departDate,
            returnDate=returnDate,
        )
        booking_instance.save()
        return redirect('about',{"booking_form":booking_instance})  # Redirect to success page or another view
    return render(request, 'index.html')

    # if request.method == "POST":
    #     print("post method")
    #     booking_form = Bookingform(request.POST)
    #
    #     if booking_form.is_valid():
    #         # Bookingmodel.objects.create(
    #         #     destination=booking_form.cleaned_data['destination_type'],
    #         #     duration=booking_form.cleaned_data['duration_type'],
    #         #     depart_date=booking_form.cleaned_data['depart_date'],
    #         #     return_date=booking_form.cleaned_data['return_date'])
    #         booking_form.save()
    #         print('booking form valid')
    #         return redirect('about')
    #     else:
    #         booking_form = Bookingform()
    #         signup_form = Signupform(request.POST)
    #         if signup_form.is_valid():
    #             name = signup_form.cleaned_data['name']
    #             email = signup_form.cleaned_data['email']
    #             return redirect('about')
    #         else:
    #             signup_form = Signupform()
    #             print('sign up form invalid')
    # else:
    #     signup_form = Signupform()
    #     booking_form = Bookingform()
    #     print('not a post method')
    #     print("outside if else")
    # return render(request, 'index.html', {
    #     # 'signup_form': signup_form,
    #     'booking_form': booking_form
    # })


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


# from django.shortcuts import render
# from .models import Bookingmodel
#
# def book_details1(request):
#     bookings = Bookingmodel.objects.all()
#     return render(request, 'NEW.html', {'bookings': bookings})
