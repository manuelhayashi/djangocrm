from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Order
from .models import Customer
from .models import Product


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['status']

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email']

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'category', 'description']
