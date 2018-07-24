from django.urls import path
from . import views

app_name= "transactions"

urlpatterns= [
    path("sale/list/", views.SaleList.as_view(), name="sale_list"),
    path("sale/new/", views.SaleView.as_view(), name="new_sale"),

    path("purchase/new/", views.PurchaseView.as_view(), name="new_purchase"),
    path("purchase/list/", views.PurchaseList.as_view(), name="purchase_list"),

    path("sale/return/new/<int:id>/", views.sale_return_view, name="new_sale_return"),
    path("sale/return/list/", views.SaleReturnList.as_view(), name="sale_return_list"),

    path("purchase/return/list/", views.PurchaseReturnList.as_view(), name="purchase_return_list"),
    path("purchase/return/new/<int:pk>/", views.purchase_return_view , name="new_purchase_return"),
]