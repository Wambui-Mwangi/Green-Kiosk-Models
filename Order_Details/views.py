from django.shortcuts import render
from Order_Details.models import Order

# Create your views here.

def orders_list(request):
    orders = Order.objects.all()
    return render (request, "Order_Details/orders_list.html", {"products": orders})