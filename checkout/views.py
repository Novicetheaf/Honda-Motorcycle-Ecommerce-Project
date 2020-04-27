from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserPaymentDetailsForm, UserAddressOrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from motorcycles.models import Motorcycle
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    if request.method == "POST":
        users_address_entry = UserAddressOrderForm(request.POST)
        users_payment_entry = UserPaymentDetailsForm(request.POST)

        if users_address_entry.is_valid() and users_payment_entry.is_valid():
            order = users_address_entry.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Motorcycle, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order = order,
                    product = product,
                    quantity = quantity
                )
                order_line_item.save()
            
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "EUR",
                    description = request.user.email,
                    card = users_payment_entry.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Sorry! your card was declined!")


            if customer.paid:
                messages.error(request, "Payment successful!")
                request.session['cart'] = {}
                return redirect(reverse('motorcycles'))
            else:
                messages.error(request, "Payment unsuccessful")
        else:
            print(users_payment_entry.errors)
            messages.error(request, "Sorry! we were unable to process your card")
    else:
        users_payment_entry = UserPaymentDetailsForm()
        users_address_entry = UserAddressOrderForm()
    
    return render(request, "checkout.html", {"users_address_entry": users_address_entry, "users_payment_entry": users_payment_entry, "publishable": settings.STRIPE_PUBLISHABLE})