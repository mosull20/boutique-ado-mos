from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KC4LtFILsTNF3oi2P59wyPVwG4ktHBczZQhwHGwqvUWsUxIpYKbJcC82G67ZJsK3XDgZR8ehyL67QgGlY9ifWMk00jz2JmhKB',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
