from django.contrib import admin
from .models import Category, Furniture, OwnerAccount

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'cat_name']

class FurnitureAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'price', 'description', 'image', 'cat_fk']

class OwnerAccountAdmin(admin.ModelAdmin):
    list_display = ['Ownercardno', 'Ownercvv', 'balance']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Furniture, FurnitureAdmin)
admin.site.register(OwnerAccount, OwnerAccountAdmin)

