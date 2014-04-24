from django.contrib import admin
from quotation.models import User, Order


class UserAdmin(admin.ModelAdmin):
    fields = ['name']


admin.site.register(User, UserAdmin)
admin.site.register(Order)