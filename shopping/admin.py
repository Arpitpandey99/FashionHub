from django.contrib import admin

# Register your models here.

from shopping.models import *

admin.site.register(User_detail)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Sub_category)
admin.site.register(Add_to_cart)
admin.site.register(Order_placed)

