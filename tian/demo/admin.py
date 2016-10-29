from django.contrib import admin

# Register your models here.
from models import *
admin.site.register(goodKinds)
admin.site.register(goodsInfo)
admin.site.register(user)
admin.site.register(user_history)
admin.site.register(user_addr)
admin.site.register(shoppingCart)
admin.site.register(order)
admin.site.register(order_goods)