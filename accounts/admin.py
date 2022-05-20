from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .form import CustomUserChangeForm,CustomUserCreateForm
from .models import CostumUser
# Register your models here.

class CustomuserAdmin(UserAdmin):
    add_form = CustomUserCreateForm
    form  = CustomUserChangeForm
    model = CostumUser
    list_display = ['email','username','first_name','last_name','age','is_staff']
    fieldsets = UserAdmin.fieldsets+(
        (None, {'fields':('age',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields':('age')}),
    )

admin.site.register(CostumUser,CustomuserAdmin)
