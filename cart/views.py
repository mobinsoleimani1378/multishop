from django.shortcuts import render, redirect

from cart.cart_moudle import Cart
from cart.models import Order, OrderItem
from product.models import Product


def cart_add(request, id):
    if request.method == 'POST':
        color = request.POST.get('color')
        size = request.POST.get('size')
        quantity = request.POST.get('quantity')
        product = Product.objects.get(id=id)
        print(color, size)
        cart = Cart(request)
        cart.add(product, color, size, quantity)
        return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})


def order_detail(request, pk):
    order = Order.objects.get(id=pk)
    return render(request, 'cart/order_detail.html', {'order': order})


def cart_delete(request, id):
    cart = Cart(request)
    cart.delete(id)
    return redirect('cart:cart_detail')


def order_create(request):
    cart = Cart(request)
    order = Order.objects.create(user=request.user, total_price=cart.total)
    for item in cart:
        OrderItem.objects.create(order=order, product=item['product'], color=item['color'], size=item['size'],
                                 quantity=item['quantity'], price=item['price'])
    cart.remove_cart()
    return redirect('cart:order_detail', order.id)
