from django.contrib import admin
from .models import Category,Product


class AdminCathegorie(admin.ModelAdmin):
    list_display = ['name','date_added']

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','date_added','price','Category']


# Register your models here.
admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCathegorie)

