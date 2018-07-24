from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from .models import Author, Publisher, Book


# Create your views here.
class CreateAuthor(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ()
    model = Author
    template_name = "books/author_create_form.html"
    fields = ("name", )


class UpdateAuthor(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ()
    model = Author
    template_name = "books/author_update_form.html"
    fields = ("name",)


class DeleteAuthor(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ()
    model = Author
    success_url = reverse_lazy("books:author_list")


class AuthorList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = ()
    model = Author
    template_name = "books/author_list.html"


class AuthorDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = ()
    model = Author
    template_name = "books/author_detail.html"


class CreateBook(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ()
    model = Book
    template_name = "books/book_create_form.html"
    fields = ("name", "author", "publisher", "isbn", "buying_price", "selling_price")


class BookUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ()
    model = Book
    template_name = "books/book_update_form.html"
    fields = ("name", "author", "publisher", "isbn", "quantity", "buying_price", "selling_price")


class BookDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ()
    model = Book
    success_url = reverse_lazy("books:list_book")


class BookDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = ()
    model = Book
    template_name = "books/book_detail.html"


class BookList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = ()
    model = Book
    template_name = "books/book_list.html"


class PublisherCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ()
    model = Publisher
    template_name = "books/publisher_create_form.html"
    fields = ("name",)


class PublisherUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ()
    model = Publisher
    template_name = "books/publisher_update_form.html"
    fields = ("name",)


class PublisherDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ()
    model = Book
    success_url = reverse_lazy("books:publisher_list")


class PublisherDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = ()
    model = Publisher
    template_name = "books/publisher_detail.html"


class PublisherList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = ()
    model = Publisher
    template_name = "books/publisher_list.html"
