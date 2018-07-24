from django.urls import path
from . import views

app_name= "transactions"

urlpatterns= [
    path("sale/list/", views.SaleList.as_view(), name="sale_list"),
    path("sale/new/", views.Sale.as_view(), name="new_sale"),

    path("purchase/new/", views.Purchase.as_view(), name="new_purchase"),
    path("purchase/list/", views.PurchaseList.as_view(), name="purchase_list"),

    path("sale/return/new/", views.SaleReturn.as_view(), name="new_sale_return"),
    path("sale/return/list/", views.SaleReturnList.as_view(), name="sale_return_list"),

    path("purchase/return/list/", views.PurchaseReturnList.as_view(), name="purchase_return_list"),
    path("purchase/return/new/", views.PurchaseReturn.as_view(), name="new_purchase_return"),
]