from django.contrib import admin
from home.models import Product
from home.models import singup
from home.models import about
# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discounted_price','selling_price', 'category', 'Product_image']


@admin.register(singup)
class singupModelAdmin(admin.ModelAdmin):
        list_display = ['first_name', 'medal_name', 'last_name','contact', 'birth_date', 'user_name','password']

admin.site.register(about)