from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Create your views here.


def view_basket(request):
    return render(request, "basket.html")


def add_to_basket(request, id):
    quantity = int(request.POST.get('quantity'))

    basket = request.session.get('basket', {})
    if id in basket:
        basket[id] = int(basket[id]) + quantity
    else:
        basket[id] = basket.get(id, quantity)

    request.session['basket'] = basket
    messages.success(request, 'Item(s) added to basket!')
    return redirect(reverse('products'))


def edit_basket(request, id):
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[id] = quantity
    else:
        basket.pop(id)

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, id):
    """Remove an item from the basket"""
    basket = request.session.get('basket', {})
    basket.pop(id)
    request.session['basket'] = basket
    return redirect(reverse('view_basket'))
