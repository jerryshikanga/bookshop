from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from books.models import Book
from customer.models import Customer
from wholesaler.models import WholeSeller
from transactions.models import Sale, Purchase, SaleReturn, PurchaseReturn
from django.utils import timezone
from django.db.models import Sum


@login_required
def index(request):
    sales_today = Sale.objects.filter(datetime_sale__day=timezone.now().day)
    purchases_today = Purchase.objects.filter(datetime_purchase__day=timezone.now().day)
    sales_today_sum = 0
    purchases_today_sum = 0
    for sale in sales_today : sales_today_sum += sale.value
    for purchase in purchases_today : purchases_today_sum += purchase.value
    context = {
        "books": Book.objects.all(),
        "customers": Customer.objects.all(),
        "whole_sellers": WholeSeller.objects.all(),
        "sales_today": sales_today,
        "sales_today_sum": sales_today_sum,
        "purchases_today": purchases_today,
        "purchases_today_sum" : purchases_today_sum,
        "sale_returns_today": SaleReturn.objects.filter(datetime_return__day=timezone.now().day),
        "purchase_returns_today": PurchaseReturn.objects.filter(datetime_return__day=timezone.now().day),

        "customers_latest": Customer.objects.all().order_by("-id")[:5]
    }
    return render(request, "index.html", context)
