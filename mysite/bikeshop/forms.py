from django import forms
from django.forms import ModelForm
from .models import Bike, Order, Comment

class BikeForm(ModelForm):
    class Meta:
        model = Bike
        fields = ['name', 'category', 'brand', 'description', 'price', 'image']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['bike', 'quantity', 'shipping_address', 'billing_address']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
