from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import CreateProductForm


@login_required
def index(request):
    return render(request, 'dashboard/index.html',)

@login_required
def staffs(request):
    return render(request, 'dashboard/staffs.html')

@login_required
def product(request):
    products = Product.objects.all()
    
    if request.method == "POST":
        form = CreateProductForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('dashboard-product')
    else:
        form = CreateProductForm()

    context = {
        'products':products,
        'form': form,
    }
    return render(request, 'dashboard/product.html',context)

@login_required
def order(request):
    return render(request, 'dashboard/order.html')