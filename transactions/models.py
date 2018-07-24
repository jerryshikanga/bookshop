from django.db import models
from books.models import Book
from django.utils import timezone
from django.contrib.auth import get_user_model
from customer.models import Customer
from wholesaler.models import WholeSeller
from bookshop.globals import ModelGetFieldsMixin

User = get_user_model()


# Create your models here.
class Sale(ModelGetFieldsMixin, models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Book")
    quantity = models.IntegerField(verbose_name="Sale Quantity")
    datetime_sale = models.DateTimeField(default=timezone.now, verbose_name="Time of Sale")
    remarks = models.TextField(verbose_name="Remarks")
    authorised_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

    class Meta(object):
        ordering = ("datetime_sale", "book")
        verbose_name = "Sale"
        verbose_name_plural = "Sales"

    def __str__(self):
        return "Sale for %s on %s"%(self.book.name, self.datetime_sale)

    @property
    def value(self):
        return self.book.selling_price * self.quantity


class Purchase(ModelGetFieldsMixin, models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Book")
    quantity = models.IntegerField(verbose_name="Purchase Quantity")
    datetime_purchase = models.DateTimeField(default=timezone.now, verbose_name="Time of Purchase")
    remarks = models.TextField(verbose_name="Remarks")
    authorised_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    whole_seller = models.ForeignKey(WholeSeller, on_delete=models.SET_NULL, null=True)

    class Meta(object):
        ordering = ("datetime_purchase", "book")
        verbose_name = "Purchase"
        verbose_name_plural = "Purchases"

    def __str__(self):
        return "Purchase for %s on %s"%(self.book.name, self.datetime_purchase)

    @property
    def value(self):
        return self.book.buying_price*self.quantity


class SaleReturn(ModelGetFieldsMixin, models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, verbose_name="Sale Details")
    datetime_return = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Sale Return on %s"%self.datetime_return


class PurchaseReturn(ModelGetFieldsMixin, models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    datetime_return = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Sale Return on %s"%self.datetime_return