from django.contrib import admin
from .models import Products, Offer


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'description')


admin.site.register(Products, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
