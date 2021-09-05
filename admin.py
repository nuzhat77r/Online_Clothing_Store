from django.contrib import admin
from .models import (
 Product,
)

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','selling_price','discounted_price','description','brand','category','Product_image']

    
# Register your models here.
