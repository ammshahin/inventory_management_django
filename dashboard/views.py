from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'dashboard/index.html',)

def staffs(request):
    return render(request, 'dashboard/staffs.html')

def product(request):
    return render(request, 'dashboard/product.html')

def order(request):
    return render(request, 'dashboard/order.html')