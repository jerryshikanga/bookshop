from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse_lazy
from bookshop.globals import ModelGetFieldsMixin

User = get_user_model()


# Create your models here.
class Author(ModelGetFieldsMixin, models.Model):
    name = models.CharField(max_length=100, verbose_name="Author Name")

    class Meta:
        ordering = ['name',]
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("books:author_detail", kwargs={"id":self.id})


class Publisher(ModelGetFieldsMixin, models.Model):
    name = models.CharField(max_length=100, verbose_name="Publisher Name")

    class Meta(object):
        ordering = ("name",)
        verbose_name = "Publisher"
        verbose_name_plural = "Publishers"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("books:publisher_detail", kwargs={"id":self.id})


class Book(ModelGetFieldsMixin, models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, verbose_name="Author")
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True, verbose_name="Publisher")
    quantity = models.IntegerField(default=0, verbose_name="Quantity in Stock")
    isbn = models.CharField(max_length=100, verbose_name="ISBN Number")
    datetime_added = models.DateTimeField(default=timezone.now, verbose_name="Date and Time Whe Registered")
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Staff Registering")
    buying_price = models.IntegerField(verbose_name="Buying Price")
    selling_price = models.IntegerField(verbose_name="Selling Price")

    class Meta(object):
        ordering = ("name", )
        verbose_name_plural = "Books"
        verbose_name = "Book"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("books:book_detail", kwargs={"id":self.id})
