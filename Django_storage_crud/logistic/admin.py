from django.contrib import admin

from .models import Product,  Stock, StockProduct

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description",)

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ("id", "address",)

@admin.register(StockProduct)
class StockProductAdmin(admin.ModelAdmin):
    list_display = ("id", "stock", "product", "quantity", "price")
