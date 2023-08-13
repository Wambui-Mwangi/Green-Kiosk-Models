from django.shortcuts import render
from Order_Details.models import Order

# Create your views here.

def orders_list(request, order_id):
    orders = Order.objects.get(id=order_id)
    cart_products = orders.basket.products.all()
    total_amount = orders.order_Total
    total_amount = sum(product.price for product in cart_products)

    context = {
        'order': orders,
        'cart_products': cart_products,
        'total_amount': total_amount,
    }
    return render (request, "Order_Details/orders_list.html", context)