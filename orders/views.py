from django.shortcuts import render, redirect

# Create your views here.
def place_order(request):
    return render(request, 'orders/place_order.html')
