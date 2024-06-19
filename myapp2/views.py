from datetime import date, timedelta

from django.db.models import Sum, F

from myapp2.models import Client, Order, Product, OrderProducts
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


def about(request):
    """Страница About."""
    return render(request, 'about.html')


def clients_list(request):
    """Список клиентов."""
    clients = Client.objects.all()
    context = {'clients': clients}
    return render(request, 'clients_list.html', context)


def client_orders(request, client_id):
    """Отображение заказов пользователя.

    :client_id: код клиента, по которому проводится выборка
    """
    client = get_object_or_404(Client, pk=client_id)
    # orders = Order.objects.prefetch_related('products').select_related('order_prods').filter(client_id=client_id)

    order_prods = OrderProducts.objects.select_related('product').select_related('order').filter(
        order__client_id=client_id).order_by('-order_id')

    order_prods = order_prods.annotate(prod_cost=F('product__price') * F('product_count'))

    context = {
        'client_name': client.client_name,
        'orders': order_prods,
    }

    return render(request, 'client_orders.html', context)



