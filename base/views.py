from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_list(request):
    category_name = request.GET.get('category')  # Get category from query parameters
    if category_name:
        products = Product.objects.filter(category__name__iexact=category_name)
    else:
        products = Product.objects.all()

    context = {
        'products': products,
        'categories': Category.objects.all(),  # Pass categories for the sidebar
    }
    return render(request, 'base/index.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'base/product_detail.html', {'product': product})
