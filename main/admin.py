from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
  
    fieldsets = [
        ("Title/date", {"fields" : ["product_title", "prodcut_published"]}),
        ("Content",{"fields":["product_content"]})
    ]



admin.site.register(Product, ProductAdmin)