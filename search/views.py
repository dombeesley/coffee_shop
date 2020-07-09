from django.shortcuts import render
from products.models import Product


def do_search(request):
    """Allows user to search for a particular product"""
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})