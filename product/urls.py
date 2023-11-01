from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('detail/<int:pk>', views.product_detail, name='detail'),
    path('category', views.category, name='category'),
    path('list', views.product_list, name='list'),
    path('listcat/<int:id>', views.product_category, name='list_cat'),

]
