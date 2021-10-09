from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'quantity', 'price', 'date_of_exp', 'available')
    fields = ('title', 'description', 'quantity', 'price', 'date_of_exp', 'available')