from django.urls import path
from . import views

app_name = "whole_seller"

urlpatterns = [
    path("create/", views.CreateWholeSeller.as_view(), name="create_whole_seller"),
    path("update/<int:id>/", views.UpdateWholeSeller.as_view(), name="update_whole_seller"),
    path("delete/<int:id>/", views.DeleteWholeSeller.as_view(), name="delete_whole_seller"),
    path("detail/<int:id>/", views.WholeSellerDetail.as_view(), name="whole_seller_detail"),
    path("list/", views.WholeSellerList.as_view(), name="whole_seller_list"),
]