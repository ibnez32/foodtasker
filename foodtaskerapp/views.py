from django.shortcuts import render

# Create your views here.

# Redirect users to homepage with home function
def home(request):
    return render(request, 'home.html', {})
