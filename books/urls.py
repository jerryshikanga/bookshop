from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("book/create/", views.CreateBook.as_view(), name="create_book"),
    path("book/update/<int:pk>/", views.BookUpdate.as_view(), name="update_book"),
    path("book/delete/<int:pk>/", views.BookDelete.as_view(), name="delete_book"),
    path("book/list/", views.BookList.as_view(), name="list_book"),
    path("book/detail/<int:pk>/", views.BookDetail.as_view(), name="book_detail"),

    path("author/create/", views.CreateAuthor.as_view(), name="author_create"),
    path("author/update/<int:pk>/", views.UpdateAuthor.as_view(), name="author_update"),
    path("author/delete/<int:pk>/", views.DeleteAuthor.as_view(), name="author_delete"),
    path("author/list/", views.AuthorList.as_view(), name="author_list"),
    path("author/detail/<int:pk>/", views.AuthorDetail.as_view(), name="author_detail"),

    path("publisher/create/", views.PublisherCreate.as_view(), name="publisher_create"),
    path("publisher/update/<int:pk>", views.PublisherUpdate.as_view(), name="publisher_update"),
    path("publisher/delete/<int:pk>/", views.PublisherDelete.as_view(), name="publisher_delete"),
    path("publisher/list/", views.PublisherList.as_view(), name="publisher_list"),
    path("publisher/detail/<int:pk>/", views.PublisherDetail.as_view(), name="publisher_detail"),
]