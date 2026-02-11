from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('carrinho/', views.cart, name='cart'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'), 
    path('biblioteca/', views.library, name='library'), 
]
