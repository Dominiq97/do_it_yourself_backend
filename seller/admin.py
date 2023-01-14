from django.contrib import admin

from .models import Seller


class SellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')


admin.site.register(Seller, SellerAdmin)
