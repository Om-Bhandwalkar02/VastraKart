from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.models import Cart, CartItem
from .models import Order, OrderItem

@login_required
def create_order(request):
    cart = Cart.objects.filter(user=request.user).first()
    if not cart or not cart.items.exists():
        return redirect('cart_detail')

    # Calculate total price and create the order
    total_price = sum(item.product.price * item.quantity for item in cart.items.all())
    order = Order.objects.create(user=request.user, total_price=total_price)

    # Create order items from cart items
    for cart_item in cart.items.all():
        OrderItem.objects.create(
            order=order,
            product=cart_item.product,
            quantity=cart_item.quantity
        )

    # Clear the cart after the order is placed
    cart.items.all().delete()

    return redirect('order_detail', order_id=order.id)

@login_required
def order_detail(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})


def orders_list(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'orders/order_list.html', context)