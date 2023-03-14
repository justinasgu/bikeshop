from django.contrib import admin
from .models import Bike, Category, Brand, Order, Comment


class BikeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'price')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_ordered', 'status', 'total_price')
    list_filter = ('status',)




class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'bike', 'content')


admin.site.register(Bike, BikeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Comment, CommentAdmin)
