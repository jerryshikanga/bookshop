from django.views.generic import FormView, ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from . forms import SaleForm, PurchaseForm
from . models import Sale, Purchase, SaleReturn, PurchaseReturn


# Create your views here.
class SaleView(FormView):
    form_class = SaleForm
    template_name = "transaction/new_sale.html"
    success_url = reverse_lazy("transactions:sale_list")

    def form_valid(self, form):
        sale = form.save(commit=False)
        sale.book.quantity -= sale.quantity
        sale.book.save()
        sale.authorised_by = self.request.user
        sale.save()
        return super(SaleView, self).form_valid(form)


class SaleList(ListView):
    queryset = Sale.objects.all()
    model = Sale
    template_name = "transaction/sale_list.html"


class PurchaseView(FormView):
    form_class = PurchaseForm
    template_name = "transaction/new_purchase.html"
    success_url = reverse_lazy("transactions:purchase_list")

    def form_valid(self, form):
        purchase = form.save(commit=False)
        purchase.book.quantity -= purchase.quantity
        purchase.book.save()
        purchase.authorised_by = self.request.user
        purchase.save()
        return super(PurchaseView, self).form_valid(form)


class PurchaseList(ListView):
    model = Purchase
    template_name = "transaction/purchase_list.html"


def purchase_return_view(request, *args, **kwargs):
    purchase = Purchase.objects.get(pk=kwargs['pk'])
    purchase_return_obj = PurchaseReturn.objects.create(
        purchase=purchase
    )
    purchase_return_obj.save()
    purchase.book.quantity += purchase.quantity
    purchase.book.save()
    return redirect(reverse_lazy("transactions:purchase_return_list"))


class PurchaseReturnList(ListView):
    model = PurchaseReturn
    template_name = "transaction/purchase_return_list.html"


def sale_return_view(request, *args, **kwargs):
    sale = Sale.objects.get(pk=kwargs['id'])
    sale_return_obj = SaleReturn.objects.create(
        sale=sale
    )
    sale_return_obj.save()
    sale.book.quantity += sale.quantity
    sale.book.save()
    return redirect(reverse_lazy("transactions:sale_return_list"))


class SaleReturnList(ListView):
    model = SaleReturn
    template_name = "transaction/sale_return_list.html"
    