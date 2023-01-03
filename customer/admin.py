from django.contrib import admin


from administrator.models import Administrator
from customer.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')


admin.site.register(Customer, CustomerAdmin)
