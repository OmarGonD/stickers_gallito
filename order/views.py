from django.shortcuts import render, get_object_or_404
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required
import json
from django.core.serializers import serialize
from django.views.generic.list import ListView
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.


def thanks_credit_card(request):
    order_number = Order.objects.latest('id').id

    total = Order.objects.latest('id').total

    costo_despacho = Order.objects.latest('id').shipping_cost

    order_items = OrderItem.objects.filter(order=Order.objects.latest('id'))

    revenue = []
    for oi in order_items:
        revenue.append(oi.price)

    revenue = sum(revenue[0:len(revenue)])

    order_items_serialized = serialize('json', order_items, fields=['id', 'sku', 'name', 'price', 'size', 'quantity'])

    # convert the serialized string to a Python object
    order_items_obj = json.loads(order_items_serialized)

    # define the target mapping
    def mapper(p):
        return {
            'id': p['pk'],
            'sku': p['fields']['sku'],
            'name': p['fields']['name'],
            'price': p['fields']['price'],
            'size': p['fields']['size'],
            'quantity': 1 #quantity de order_item, no la cantidad de stickers. esto para que google analytics calcule correctamente el product revenue
        }

    # re-map and re-serialize the items
    order_items = json.dumps(list(map(mapper, order_items_obj)))

    response = render(request, 'thanks_credit_card.html', dict(order_number=order_number, total=total, revenue = revenue,
                                                                   order_items=order_items, costo_despacho=costo_despacho))
    return response


def thanks_deposit_payment(request):

    transaction = Order.objects.latest('id')
    order_items = OrderItem.objects.filter(order=transaction) #get jsonied for Google Analytics, useless in template
    order_items_for_template = OrderItem.objects.filter(order=transaction)
    order_number = Order.objects.latest('id').id

    
    '''sending the order to the customer'''
    subject = 'Stickers Gallito Perú - Nueva orden #{}'.format(transaction.id)
    to = ['{}'.format(transaction.email), 'stickersgallito@gmail.com', 'oma.gonzales@gmail.com']
    from_email = 'stickersgallito@stickersgallito.pe'
    order_information = {
        'transaction': transaction,
        'order_items': order_items
    }
    
    revenue = []
    for oi in order_items:
        revenue.append(oi.price)

    revenue = sum(revenue[0:len(revenue)])

    costo_despacho = Order.objects.latest('id').shipping_cost

    order_items_serialized = serialize('json', order_items, fields=['id', 'sku', 'name', 'price', 'size', 'quantity'])

    # convert the serialized string to a Python object
    order_items_obj = json.loads(order_items_serialized)

    # define the target mapping
    def mapper(p):
        return {
            'id': p['pk'],
            'sku': p['fields']['sku'],
            'name': p['fields']['name'],
            'price': p['fields']['price'],
            'size': p['fields']['size'],
            'quantity': 1 #quantity de order_item, no la cantidad de stickers. esto para que google analytics calcule correctamente el product revenue
        }

    # re-map and re-serialize the items
    order_items = json.dumps(list(map(mapper, order_items_obj)))

    response = render(request, 'thanks_deposit_payment.html', dict(order_number = order_number, transaction=transaction, revenue = revenue,
                                                                   order_items=order_items, costo_despacho = costo_despacho,
                                                                   order_items_for_template=order_items_for_template))
    return response



@login_required()
def orderHistory(request):
    if request.user.is_authenticated:
        email = str(request.user.email)
        print(email)
        order_details = Order.objects.filter(email=email)
        # order_details = get_object_or_404(Order, emailAddress=email)
        if not order_details:
            print("No hay orden")
        else:
            order_details
            print("Hay orden")
            print(order_details)
    return render(request, 'order/orders_list.html', {'order_details': order_details})


@login_required()
def viewOrder(request, order_id):
    if request.user.is_authenticated:
        email = str(request.user.email)
        order = Order.objects.get(id = order_id, email=email)
        order_items = OrderItem.objects.filter(order = order)
    return render(request, 'order/order_detail.html', {'order': order,
                                                       'order_items': order_items})


def revenue(request, year, month):
    orders = Order.objects.all()
    orders_revenue_by_month = Order.objects.all().filter()
    orders_set = Order.objects.filter(created__month=9).filter(status == 'recibido_pagado')

    revenue = 0

    for order in order_set:
        revenue += order.total - order.shipping_cost
    ### Así se filtra una fecha ###
    #Order.objects.filter(created__date=datetime.date(2019,9,27)) 
    ## Por año:
    #Order.objects.filter(created__year=2019) 
    ### Por mes y año:
    ###Order.objects.filter(created__month=9)
    return render(request, 'order/revenue.html', {'revenue': revenue})


#####################
### Catalogo View ###
#####################

from django.db.models import F, Sum

class OrdersListView(PermissionRequiredMixin,ListView):

    model = Order
    permission_required = 'is_staff'
    template_name = "order/revenue.html"
    paginate_by = 10

    def get_queryset(self):
        filter_month = self.request.GET.get('filtromes', '0')
        if filter_month == "0":
            return Order.objects.filter(status = 'recibido_pagado')
        else:
            return (Order.objects
                .filter(created__month=filter_month, status = 'recibido_pagado'))

    def get_context_data(self, **kwargs):
        context = super(OrdersListView, self).get_context_data(**kwargs)
        qs = kwargs.pop('object_list', self.object_list)
        order = self.request.GET.get('orderby', 'created')
        context = {}
        revenue = qs.aggregate(revenue=Sum('total'))
        if revenue is None:
            revenue = 0
        else:
            revenue = float(revenue['revenue']) #necessary to properly render in template / not as Decimal    
        revenue_no_shipping = qs.aggregate(revenue_no_shipping=Sum(F('total') - F('shipping_cost')))
        if revenue_no_shipping is None:
            revenue_no_shipping = 0
        else:
            revenue_no_shipping = float(revenue_no_shipping['revenue_no_shipping']) #necessary to properly render in template / not as Decimal
        context['revenue'] = revenue
        context['revenue_no_shipping'] = revenue_no_shipping
        context['filtromes'] = self.request.GET.get('filtromes', '0')
        context['orderby'] = self.request.GET.get('orderby', 'created')
        context['category'] = "catalogo"
        return context


# View for Ordenes/Ingresos
# O se puede manejar con la lista de arriba 

# class IngresosPorOrdenes(ListView):

#     model = Order
#     template_name = "shop/catalogo.html"
#     paginate_by = 10        