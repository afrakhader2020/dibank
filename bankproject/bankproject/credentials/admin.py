from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Register,Login

@admin.register(Login)
class login(admin.ModelAdmin):
    list_display=('uname',)

@admin.register(Register)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'dob', 'age', 'gender', 'phno', 'mailid', 'address', 'district', 'account_type')
    list_filter = ('gender', 'account_type')
    search_fields = ('name', 'mailid')


