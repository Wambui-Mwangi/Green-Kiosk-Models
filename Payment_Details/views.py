from django.shortcuts import render
from Order_Details.models import Order

def choose_payment(request, order_id):
    order = Order.objects.get(id=order_id)

    # context = {
    #     'order': order,
    # }
    return render(request, 'payment/choose_payment.html', {'Order': Order})

# Create your views here.
