from django.contrib import admin
from .models import ZtrUser, Devices, Product

# Register your models here.

admin.site.register(ZtrUser)
admin.site.register(Devices)
admin.site.register(Product)