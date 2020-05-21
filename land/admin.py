from django.contrib import admin
from land.models import Product


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
