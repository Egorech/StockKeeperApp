from django.contrib import admin
from .models import StorageLocation, Product, Shelf, InventoryManagementTask

@admin.register(StorageLocation)
class StorageLocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'max_weight_capacity']
    search_fields = ['name']
    list_filter = ['name']
    fields = ['name', 'max_weight_capacity']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']
    fields = ['name']

@admin.register(Shelf)
class ShelfAdmin(admin.ModelAdmin):
    list_display = ['location', 'product', 'current_quantity']
    search_fields = ['location__name', 'product__name']
    list_filter = ['location', 'product']
    fields = ['location', 'product', 'current_quantity']

@admin.register(InventoryManagementTask)
class InventoryManagementTaskAdmin(admin.ModelAdmin):
    list_display = ['task_status', 'user', 'result']
    search_fields = ['task_status', 'user__username']
    list_filter = ['task_status']
    fields = ['task_status', 'user', 'result']