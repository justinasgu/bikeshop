from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    # Bike list view
    path('bike_list/', views.BikeListView.as_view(), name='bike_list'),
    # Bike detail view with comment form
    path('<int:pk>/', views.BikeDetailView.as_view(), name='bike_detail'),
    # Bike search view
    # path('search/', views.BikeSearchView.as_view(), name='bike_search'),
    # Category list view
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    # Category detail view
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    # Brand list view
    path('brands/', views.BrandListView.as_view(), name='brand_list'),
    # Brand detail view
    path('brands/<int:pk>/', views.BrandDetailView.as_view(), name='brand_detail'),
    # Order create view
    path('order/create/', views.OrderCreateView.as_view(), name='order_create'),
    # User orders list view
    path('orders/', views.OrderListView.as_view(), name='order_list'),
    # Order detail view
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    # Order update view
    path('order/<int:pk>/create/', views.OrderUpdateView.as_view(), name='order_update'),
    # Order delete view
    path('order/<int:pk>/delete/', views.OrderDeleteView.as_view(), name='order_delete'),

    path('search/', views.search, name='search'),
]
