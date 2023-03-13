from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    # Bike list view
    path('bike_list/', views.BikeListView.as_view(), name='bike_list'),
    # Bike detail view with comment form
    path('<int:pk>/', views.BikeDetailView.as_view(), name='bike_detail'),
    # # Bike create view
    # path('bike/create/', views.BikeCreateView.as_view(), name='bike_create'),
    # # Bike update view
    # path('bike/<int:pk>/update/', views.BikeUpdateView.as_view(), name='bike_update'),
    # # Bike delete view
    # path('bike/<int:pk>/delete/', views.BikeDeleteView.as_view(), name='bike_delete'),
    # # Order create view
    # path('bike/<int:bike_id>/order/', views.order_create, name='order_create'),
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
]
