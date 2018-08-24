from django.contrib import admin
from apps.store.models import Category, Product, Customers

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]
 
admin.site.register(Category, CategoryAdmin)
 
 
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'bldurl', 'price', 'stock', 'available', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'stock', 'available']

 
admin.site.register(Product, ProductAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'address', 'city', 'state', 'zip', 'created_at', 'updated_at']
    list_filter = ['first_name', 'last_name']

 
admin.site.register(Customers, CustomerAdmin)