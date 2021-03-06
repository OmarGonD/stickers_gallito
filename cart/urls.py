from django.urls import path
from . import views

app_name = 'carrito_de_compras'

urlpatterns = [
    # path('add/<int:product_id>/', views.add_cart, name = 'add_cart'),
    path('', views.cart_detail, name='cart_detail'),
    # path('remove/<int:cart_item_id>/', views.cart_remove, name = 'cart_remove'),
    path('full_remove/<int:cart_item_id>/', views.full_remove, name='full_remove'),
    path('full_remove_sample/<int:sample_item_id>/', views.full_remove_sample, name='full_remove_sample'),
    path('full_remove_pack/<int:pack_item_id>/', views.full_remove_pack, name='full_remove_pack'),
    path('full_remove_unitary_product/<int:unitary_product_item_id>/', views.full_remove_unitary_product, name='full_remove_unitary_product'),
    path('charge_credit_card/', views.cart_charge_credit_card, name='cart_charge_credit_card'),
    path('charge_deposit_payment/', views.cart_charge_deposit_payment, name='cart_charge_deposit_payment'),


]
