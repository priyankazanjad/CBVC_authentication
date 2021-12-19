from django.contrib import admin
from .models import Orders

class OrdersAdmin(admin.ModelAdmin):
    list_display = ['company','model_name','ram','rom','processor','price','weight']
admin.site.register(Orders,OrdersAdmin)

# Register your models here.
