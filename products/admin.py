from django.contrib import admin
from .models import Category,Brand,Product,CartItem,Wishlist


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "parent", "is_active", "created_at")
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "brand", "price", "stock", "is_active")
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(CartItem)
admin.site.register(Wishlist)