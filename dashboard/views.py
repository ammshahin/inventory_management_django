from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'dashboard/index.html',)

def staffs(request):
    return render(request, 'staffs.html')
