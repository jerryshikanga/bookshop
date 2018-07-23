from django.db import models


# Create your models here.
class WholeSeller(models.Model):
    name = models.CharField(max_length=100, verbose_name="Whole Seller Name")
    address = models.CharField(max_length=250, verbose_name="Whole Seller Address")

    class Meta(object):
        ordering = ("name",)
        verbose_name = "Whole Seller"
        verbose_name_plural = "Whole Sellers"

    def __str__(self):
        return self.name