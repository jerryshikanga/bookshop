from django.urls import reverse_lazy
from .models import WholeSeller
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Create your views here.
class CreateWholeSeller(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ()
    model = WholeSeller
    template_name = "wholesaler/wholesaler_create_form.html"
    fields = ("name", "address",)


class UpdateWholeSeller(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ()
    model = WholeSeller
    template_name = "wholesaler/wholeseller_update_form.html"
    fields = ("name", "address",)


class DeleteWholeSeller(LoginRequiredMixin, PermissionRequiredMixin,DeleteView):
    permission_required = ()
    model = WholeSeller
    success_url = reverse_lazy("whole_seller:whole_seller_list")


class WholeSellerList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = ()
    model = WholeSeller
    template_name = "wholesaler/wholeseller_list.html"


class WholeSellerDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = ()
    model = WholeSeller
    template_name = "wholesaler/wholeseller_detail.html"
