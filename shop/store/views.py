import stripe
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

from shop.settings import STRIPE_PUBLISHABLE_KEY, STRIPE_SECRET_KEY
from store.models import Item


class ItemPage(TemplateView):
    """View for item's page"""
    template_name = 'item.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ItemPage, self).get_context_data(*args, **kwargs)
        item_id = self.kwargs.get("item_id")
        item = get_object_or_404(Item, id=item_id)
        context['title'] = f'Buy Item {item.name}'
        context['name'] = item.name
        context['price'] = item.price / 100
        context['description'] = item.description
        return context


stripe.api_key = STRIPE_SECRET_KEY


@csrf_exempt
def BuyItem(request,  *args, **kwargs):
    """View for redirect to buy on stripe"""
    item_id = kwargs.get("item_id")
    item = get_object_or_404(Item, id=item_id)
    domain_url = 'http://127.0.0.1:8000/'
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': item.price,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=domain_url + 'success/',
        cancel_url=domain_url + 'item/' + str(item_id),
    )
    return redirect(session.url, code=303)


@csrf_exempt
def stripe_config(request):
    """View for get STRIPE_PUBLISHABLE_KEY"""
    if request.method == 'GET':
        stripe_config = {'publicKey': STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


class SuccessView(TemplateView):
    """View for succces page"""
    template_name = 'success.html'
