from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product


@login_required
def index(request):
    return render(request, 'dashboard/index.html',)

@login_required
def staffs(request):
    return render(request, 'dashboard/staffs.html')

@login_required
def product(request):
    products = Product.objects.all()
    context = {
        'products':products,
    }
    return render(request, 'dashboard/product.html',context)

@login_required
def order(request):
    return render(request, 'dashboard/order.html')