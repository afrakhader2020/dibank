from django.contrib import admin

# Register your models here.
from .models import branches, district


class districtAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(district,districtAdmin)

class branchesAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(branches,branchesAdmin)


