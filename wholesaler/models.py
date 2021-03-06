from django.db import models
from django.urls import reverse_lazy
from bookshop.globals import ModelGetFieldsMixin


# Create your models here.
class WholeSeller(ModelGetFieldsMixin, models.Model):
    name = models.CharField(max_length=100, verbose_name="Whole Seller Name")
    address = models.CharField(max_length=250, verbose_name="Whole Seller Address")

    class Meta(object):
        ordering = ("name",)
        verbose_name = "Whole Seller"
        verbose_name_plural = "Whole Sellers"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("whole_seller:whole_seller_detail", kwargs={"id":self.id})
