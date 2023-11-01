from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from cart.cart_moudle import Cart
from product.models import Product, Category, Comment


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        body = request.POST.get('body')
        parent_id = request.POST.get('parent_id')
        Comment.objects.create(body=body, product=product, user=request.user, parent_id=parent_id)

    if product.review == 0:
        product.review = 1
        product.save()
    else:
        product.review = product.review + 1
        product.save()
    return render(request, 'product/product_detail.html', {'product': product})


def product_list(request):
    product = Product.objects.all()
    categories = Category.objects.all()
    categorys = []
    for i in categories:
        if not i.parent:
            if i.catt.all():
                categorys.append(i)
    cat = request.GET.getlist('cat')
    colors = request.GET.getlist('color')
    sizes = request.GET.getlist('size')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    q = request.GET.get('q')
    if cat:
        product = product.filter(category__title__in=cat).distinct()

    if min_price and max_price:
        product = product.filter(price__gte=min_price, price__lte=max_price).distinct()
    if colors:
        product = product.filter(color__title__in=colors).distinct()
    if sizes:
        product = product.filter(size__title__in=sizes).distinct()
    if q:
        product = product.filter(title__icontains=q).distinct()

    page_number = request.GET.get('page')
    paginator = Paginator(product, 1)
    object_list = paginator.get_page(page_number)

    return render(request, 'product/product_list.html', {'products': object_list, 'categorys': categorys})


def category(request):
    categoroies = Category.objects.all()
    product = Product.objects.get(id=1)
    cart = Cart(request)

    return render(request, 'includes/navbar.html', {'categoroies': categoroies, 'product': product, 'cart': cart})


def product_category(request, id):
    category = Category.objects.get(id=id)
    product_cat = category.catt.all()

    return render(request, 'product/product_list.html', {'products': product_cat})

    # def show_all_product_page(request):
    #     context = {}
    #
    #     filtered_product = ProductFilter(
    #         request.GET,
    #         queryset=Product.objects.all()
    #     )
    #
    #     context['filtered_product'] = filtered_product
    #
    #     paginator = Paginator(filtered_product.qs, 1)
    #     page_number = request.GET.get('page')
    #     object_list = paginator.get_page(page_number)
    #
    #     context['product_page_obj'] = object_list
    #     return render(request, 'product/product_list.html', context=context)

    #
    # def test(request):
    #     print(1000)
    #     return JsonResponse({'key': True})
#
# def like(request, slug, pk):
#     try:
#         like = Like.objects.get(product__slug=slug, user_id=request.user.id)
#         like.delete()
#         # return JsonResponse({"response": "unliked"})
#     except:
#         Like.objects.create(product__id=pk, user_id=request.user.id)
#         # return JsonResponse({"response": "unliked"})
#     return redirect('product:detail', slug, id)
