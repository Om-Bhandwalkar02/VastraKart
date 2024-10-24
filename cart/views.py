from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from base.models import Product
from .models import Cart, CartItem

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1  # Increment quantity
    cart_item.save()

    return redirect('cart_detail')

@login_required
def remove_from_cart(request, product_id):
    cart = Cart.objects.filter(user=request.user).first()
    if cart:
        cart_item = CartItem.objects.filter(cart=cart, product__id=product_id).first()
        if cart_item:
            cart_item.delete()  # Remove the item

    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart = Cart.objects.filter(user=request.user).first()

    cart_items = [
        {
            'product': item.product,
            'quantity': item.quantity,
            'total_price': item.product.price * item.quantity,
        }
        for item in cart.items.all()
    ] if cart else []

    return render(request, 'cart/cart_detail.html', {'cart_items': cart_items})
