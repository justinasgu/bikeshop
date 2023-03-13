from django import forms
from .models import Bike, Order, Comment, User, Profilis


class BikeForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = ['name', 'category', 'brand', 'description', 'price', 'image']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['bike', 'quantity', 'shipping_address', 'billing_address']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class UserUpdateForm(forms.ModelForm):
    # email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfilisUpdateForm(forms.ModelForm):
    class Meta:
        model = Profilis
        fields = ['nuotrauka']
