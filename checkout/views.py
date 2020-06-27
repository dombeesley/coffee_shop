from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order_form.instance.user = request.user
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            basket = request.session.get('basket', {})
            total = 0
            for id, quantity in basket.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity
                )
                order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="GBP",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Sorry, but your card was declined")

            if customer.paid:
                messages.error(request, "Hurrah! You've successfully paid!")
                request.session['basket'] = {}
                return redirect(reverse('products'))
            else:
                messages.error(request, "We're unable to take your payment right now")
        else:
            print(payment_form.errors)
            messages.error(request, "Sorry, we couldn't take a payment with that card - would you like to try again?")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(request, "checkout.html", {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})
