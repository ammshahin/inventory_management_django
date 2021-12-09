from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('staffs/', views.staffs, name='dashboard-staffs'),
    path('product/', views.product, name='dashboard-product'),
    path('order/', views.order, name='dashboard-order')
]