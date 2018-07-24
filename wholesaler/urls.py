from django.urls import path
from . import views

app_name = "whole_seller"

urlpatterns = [
    path("create/", views.CreateWholeSeller.as_view(), name="create_whole_seller"),
    path("update/<int:pk>/", views.UpdateWholeSeller.as_view(), name="update_whole_seller"),
    path("delete/<int:pk>/", views.DeleteWholeSeller.as_view(), name="delete_whole_seller"),
    path("detail/<int:pk>/", views.WholeSellerDetail.as_view(), name="whole_seller_detail"),
    path("list/", views.WholeSellerList.as_view(), name="whole_seller_list"),
]