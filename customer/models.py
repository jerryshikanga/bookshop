from django.db import models
from django.urls import reverse_lazy
from bookshop.globals import ModelGetFieldsMixin


# Create your models here.
class Customer(ModelGetFieldsMixin, models.Model):
    name = models.CharField(max_length=100, verbose_name="Customer Name")
    address = models.CharField(max_length=100, verbose_name="Contact Address")

    class Meta(object):
        ordering = ("name",)
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("customer:customer_detail", kwargs={"pk":self.pk})
