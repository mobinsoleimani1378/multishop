from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('detail', views.cart_detail, name='cart_detail'),
    path('add/<int:id>', views.cart_add, name='cart_add'),
    path('order/<int:pk>', views.order_detail, name='order_detail'),
    path('ordercreate', views.order_create, name='order_create'),
    path('deletecart/<str:id>', views.cart_delete, name='delete_cart'),

]
