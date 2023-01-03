from django.contrib import admin

from administrator.models import Administrator


class AdministratorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')


admin.site.register(Administrator, AdministratorAdmin)
