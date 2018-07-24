from django.urls import path
from . import views

app_name = "customer"

urlpatterns = [
    path("create/", views.CreateCustomer.as_view(), name="customer_create"),
    path("list/", views.CustomerList.as_view(), name="customer_list"),
    path("detail/<int:pk>/", views.CustomerDetail.as_view(), name="customer_detail"),
    path("update/<int:pk>/", views.UpdateCustomer.as_view(), name="customer_update"),
    path("delete/<int:pk>/", views.CustomerDelete.as_view(), name="customer_delete"),
]