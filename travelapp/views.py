from django.shortcuts import render, redirect
from .forms import Signupform


# Create your views here.
def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def signUpFormData(request):
    if request.method == 'POST':
        data = Signupform(request.POST)
        if data.is_valid():
            # Signupform.objects.create(
            #     name=form.cleaned_data['name'],
            #     email=form.cleaned_data['email']
            # )
            return redirect('index')  # Redirect to a success page or another view
    else:
        data = Signupform()
    print("dataaaaa")
    return render(request, 'index.html', {"form": data})
