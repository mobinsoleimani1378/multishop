from django.shortcuts import render
from product.models import Product, Category


def home(request):
    products = Product.objects.all()
    category = Category.objects.all()
    recent_products = Product.objects.all()[:2]
    list = [10000000]

    for product in products:
        list.append(product.review)
    list.sort()
    popular = []
    for i in list[-4:-1]:
        x = Product.objects.get(review=i)
        popular.append(x)

    return render(request, 'home/home.html',
                  {'products': products, "categories": category, 'recent_products': recent_products,
                   'popular': popular})
