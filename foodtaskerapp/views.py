from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

# Redirect users to homepage with home function
def home(request):
    return redirect(restaurant_home)


# First ask users for login information in sign in page, before going to the home page.
@login_required(login_url='/restaurant/sign-in/')
def restaurant_home(request):
    return render(request, 'restaurant/home.html', {})

def restaurant_sign_up(request):
    return render (request, 'restaurant/sign_up.html', {})
