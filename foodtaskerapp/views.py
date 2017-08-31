from django.shortcuts import render, redirect

def home(request):
    return redirect(restaurant_home)

def restaurant_home(request):
    return render(request, 'restaurant/home.html')
