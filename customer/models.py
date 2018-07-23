from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Customer Name")
    address = models.CharField(max_length=100, verbose_name="Contact Address")

    class Meta(object):
        ordering = ("name",)
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.name