from django.shortcuts import render
from .forms import ProductCartForm
from Cart_Details.models import Product
from Cart_Details.models import Cart


def product_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    if created:
        cart.save()
    cart.products.add(product)
    context = {
        'product': product,
        'cart' : Cart,
        'added_to_cart' : True,
    }
    return render(request, "Cart_Details/product_cart.html", context)
    # return render (request, "Cart_Details/product_cart.html", {"products": product})


