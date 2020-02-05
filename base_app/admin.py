from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import ZtrUserCreationForm, ZtrUserChangeForm
from .models import ZtrUser, Devices, Product


class ZtrUserAdmin(UserAdmin):
    model = ZtrUser
    add_form = ZtrUserCreationForm
    form = ZtrUserChangeForm


admin.site.register(ZtrUser, ZtrUserAdmin)
admin.site.register(Devices)
admin.site.register(Product)
