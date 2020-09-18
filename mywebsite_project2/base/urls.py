from django.urls import path
# from django.http import HttpResponse
# from django.utils.html import escape
from . import views

urlpatterns = [
    path('', views.home, name="home"), # trigger the functions
    path('products/', views.products, name="products"), # trigger the functions
    path('customer_orders/<int:id>', views.customerOrders, name='customer_orders'), # trigger the functions
    path('customers/', views.customerList, name='customers'),
    path('orders/', views.orderList, name='orders'),

    path('gridtest/', views.readData, name="gridtest"), # test page

    path('create_order/', views.createOrder, name="create_order"),
    path('create_customer/', views.createCustomer, name="create_customer"),
    path('create_product/', views.createProduct, name="create_product"),
    path('update_order/<int:id>', views.updateOrder, name="update_order"),
    path('update_customer/<int:id>', views.updateCustomer, name="update_customer"),
    path('update_product/<int:id>', views.updateProduct, name="update_product"),
    path('delete_item/<int:id>', views.deleteOrder, name='delete_item'),
    path('delete_product/<int:id>', views.deleteProduct, name='delete_product'),

    path('register/', views.registerForm, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),


]
