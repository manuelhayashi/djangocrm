from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Product
from . models import Order
from . models import Customer
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from . forms import CreateUserForm
from . forms import OrderForm
from . forms import CustomerForm
from . forms import ProductForm

from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required




# Create your views here.

@login_required(login_url='login')
def home(request):
    orders = Order.objects.all()

    total_orders = orders.count()
    processing = orders.filter(status='Processing').count()
    shipped = orders.filter(status='Shipped').count()
    delivered = orders.filter(status='Delivered').count()
    returned = orders.filter(status='Returned').count()
    context = {'orders': orders,
                'total_orders': total_orders, 'processing': processing,
                'shipped': shipped, 'delivered': delivered, 'returned': returned}
    return render(request, 'base/status.html', context)

@login_required(login_url='login')
def products(request):
    products = Product.objects.all()
    return render(request, 'base/products.html', {'products': products})

@login_required(login_url='login')
def customerOrders(request, id):
    customer = Customer.objects.get(pk=id)
    orders = customer.order_set.all()
    order_count = orders.count()

    context = {'customer': customer, 'orders': orders, 'order_count': order_count}
    return render(request, 'base/customer_orders.html', context)

@login_required(login_url='login')
def customerList(request):
    customers = Customer.objects.all()
    total_customers = customers.count()

    context = {'customers': customers, 'total_customers': total_customers}
    return render(request, 'base/customers.html', context)

@login_required(login_url='login')
def orderList(request):
    orders = Order.objects.all()

    context = {'orders': orders}
    return render(request, 'base/order_list.html', context)

def registerForm(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()    #creates a new user
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('home')

    context = {'form': form}
    return render(request, 'base/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'base/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        # print('Printing POST :', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'base/order_form.html', context)

@login_required(login_url='login')
def createCustomer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/customers')
    context = {'form': form}
    return render(request, 'base/customer_form.html', context)

@login_required(login_url='login')
def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/products')
    context = {'form': form}
    return render(request, 'base/product_form.html', context)

@login_required(login_url='login')
def updateOrder(request, id):
    order = Order.objects.get(pk=id)
    form = OrderForm(instance=order)

    if request.method =='POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/orders')

    context = {'form': form}
    return render(request, 'base/order_form.html', context)


def gridtest(request):
    return render(request, 'base/grid_test.html')


def readData(request):
    context = {}

    if request.method == 'POST':
        print('Post from Grid ...:', request.POST)
        return redirect('/')

    return render(request, 'base/grid_test.html', context)

@login_required(login_url='login')
def deleteOrder(request, id):
    order = Order.objects.get(pk=id)

    if request.method == "POST":
        order.delete()
        return redirect('/orders')

    context = {'item': order}
    return render(request, 'base/delete_order.html', context)

@login_required(login_url='login')
def deleteProduct(request, id):
    product = Product.objects.get(pk=id)

    if request.method == "POST":
        product.delete()
        return redirect('/products')

    context = {'item': product}
    return render(request, 'base/delete_product.html', context)

@login_required(login_url='login')
def updateCustomer(request, id):
    customer = Customer.objects.get(pk=id)
    form = CustomerForm(instance=customer)

    if request.method =='POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/customers')

    context = {'form': form}
    return render(request, 'base/customer_form.html', context)

@login_required(login_url='login')
def updateProduct(request, id):
    product = Product.objects.get(pk=id)
    form = ProductForm(instance=product)

    if request.method =='POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            print(form)

            form.save()
            return redirect('/products/')

    context = {'form': form}
    return render(request, 'base/product_form.html', context)