from django.shortcuts import render, redirect
from .forms import ProductCartForm
from Cart_Details.models import Product
from Cart_Details.models import Cart


def product_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart.products.add(product)
    cart.save()

    return redirect('cart_contents_view') 

def cart_contents(request):
    user_cart = Cart.objects.get(user=request.user)
    cart_products = user_cart.products.all()
    total_price = sum(product.price for product in cart_products)

    context = {
        'cart_products': cart_products,
        'total_price': total_price,
    }
    
    return render(request, 'Cart_Details/cart_contents.html', context)