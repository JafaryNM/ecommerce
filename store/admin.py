from django.contrib import admin
from .models import Category,Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulate_field={'slug':('name',)}
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','instock','price','created_date','update_date']
    list_filter=['instock','isactive']
    list_editable=['instock','price']
    prepopulate_field={'slug':('title',)}

