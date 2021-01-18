from django.contrib import admin
from .models import item, orderItem, order


admin.site.register(item)
admin.site.register(orderItem)
admin.site.register(order)
