from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import User2, Product2, Order2
import datetime


def user_products(request, user_id, days):
    user = get_object_or_404(User2, pk=user_id)
    orders = Order2.objects.filter(customer=user, date_ordered__gte=timezone.now() - datetime.timedelta(days=days))
    products = set()

    for order in orders:
        products.update(order.products.all())

    context = {'user': user, 'days': days, 'products': products}
    return render(request, 'homework2/user_products.html', context)

