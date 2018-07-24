from django.contrib import admin
from . models import Sale, Purchase, SaleReturn, PurchaseReturn

# Register your models here.
admin.site.register(Sale)
admin.site.register(Purchase)
admin.site.register(SaleReturn)
admin.site.register(PurchaseReturn)