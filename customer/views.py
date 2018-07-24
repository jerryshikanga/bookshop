from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth import mixins
from .models import Customer


# Create your views here.
class CreateCustomer(mixins.LoginRequiredMixin, mixins.PermissionRequiredMixin, CreateView):
    permission_required = ()
    model = Customer
    fields = ("name", "address")
    template_name = "customer/customer_create_form.html"


class UpdateCustomer(mixins.LoginRequiredMixin, mixins.PermissionRequiredMixin, UpdateView):
    permission_required = ()
    model = Customer
    fields = ("name", "address")
    template_name = "customer/customer_update_form.html"


class CustomerDelete(mixins.LoginRequiredMixin, mixins.PermissionRequiredMixin, DeleteView):
    permission_required = ()
    model = Customer
    success_url = reverse_lazy("customer:customer_list")


class CustomerDetail(mixins.LoginRequiredMixin, mixins.PermissionRequiredMixin, DetailView):
    permission_required = ()
    model = Customer
    template_name = "customer/customer_detail.html"


class CustomerList(mixins.LoginRequiredMixin, mixins.PermissionRequiredMixin, ListView):
    permission_required = ()
    model = Customer
    template_name = "customer/customer_list.html"
