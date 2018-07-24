from django.views.generic import FormView, ListView
from django.urls import reverse_lazy
from . forms import SaleForm, PurchaseForm, SaleReturnForm, PurchaseReturnForm


# Create your views here.
class Sale(FormView):
    form_class = SaleForm
    template_name = "transaction/new_sale.html"
    success_url = reverse_lazy("transactions:sale_list")

    def form_valid(self, form):
        form.perform_sale()
        return super(Sale, self).form_valid()


class SaleList(ListView):
    model = Sale
    template_name = "transaction/sale_list.html"


class Purchase(FormView):
    form_class = PurchaseForm
    template_name = "transaction/new_purchase.html"
    success_url = reverse_lazy("transactions:purchase_list")

    def form_valid(self, form):
        form.perform_purchase()
        return super(Purchase, self).form_valid()


class PurchaseList(ListView):
    model = Purchase
    template_name = "transaction/purchase_list.html"


class PurchaseReturn(FormView):
    form_class = PurchaseReturnForm
    success_url = reverse_lazy("transactions:purchase_return_list")

    def form_valid(self, form):
        form.perform_purchase_return()
        super(PurchaseReturn, self).form_valid()


class PurchaseReturnList(ListView):
    model = PurchaseReturn
    template_name = "transaction/purchase_return_list.html"


class SaleReturn(FormView):
    form_class = SaleReturnForm
    success_url = reverse_lazy("transactions:sale_return_list")

    def form_valid(self, form):
        form.perform_sale_return()
        return super(SaleReturn, self).form_valid()


class SaleReturnList(ListView):
    model = SaleReturn
    template_name = "transaction/sale_return_list.html"
    