from django.urls import path

from store.views import BuyItem, ItemPage, SuccessView, stripe_config

app_name = 'store'

urlpatterns = [
    path('item/<int:item_id>/', ItemPage.as_view(), name='item'),
    path('buy/<int:item_id>/', BuyItem, name='buy'),
    path('config/', stripe_config),
    path('success/', SuccessView.as_view(), name='success'),
]
