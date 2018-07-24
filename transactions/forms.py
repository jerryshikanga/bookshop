from django import forms
from books.models import Book
from customer.models import Customer
from wholesaler.models import WholeSeller
from .models import Sale, Purchase, SaleReturn, PurchaseReturn


class SaleForm(forms.Form):
    book = forms.ModelChoiceField(Book, required=True, help_text="Choose Book")
    quantity = forms.IntegerField(max_value=100, help_text="Enter Number of books to be sold")
    customer = forms.ModelChoiceField(Customer, required=False, help_text="Choose Customer")
    remarks = forms.CharField(widget=forms.Textarea, required=False, help_text="Enter additional comment/remarks on sale")

    def perform_sale(self):
        data = self.data
        book = data.book
        book.quantity -= data.quantity
        book.save()

        sale = Sale.objects.create(
            book=data.book,
            quantity=data.quantity,
            customer=data.customer,
            remarks=data.remarks,
        )
        sale.save()

        return sale


class PurchaseForm(forms.Form):
    book = forms.ModelChoiceField(Book, required=True, help_text="Choose Book")
    quantity = forms.IntegerField(max_value=100, help_text="Enter Number of books to be purchased")
    whole_seller = forms.ModelChoiceField(WholeSeller, required=False, help_text="Choose Whole Seller")
    remarks = forms.CharField(widget=forms.Textarea, required=False, help_text="Enter additional comment/remarks on sale")

    def perform_purchase(self):
        data = self.data
        book = self.book
        book.quantity += data.quantity
        book.save()

        purchase = Purchase.objects.create(
            book=data.book,
            quantity=data.quantity,
            whole_seller=data.whole_seller,
            remarks=data.remarks,
        )
        purchase.save()
        return purchase


class SaleReturnForm(forms.Form):
    sale = forms.ModelChoiceField(Sale, required=True, help_text="Choose Sale")

    def perform_sale_return(self):
        data = self.data
        sale_return = SaleReturn.objects.create(
            sale=data.sale,
        )
        book = data.sale.book
        book.quantity += data.sale.quantity
        book.save()

        sale_return.save()
        return sale_return


class PurchaseReturnForm(forms.Form):
    purchase = forms.ModelChoiceField(Purchase, required=True, help_text="Choose Purchase")

    def perform_purchase_return(self):
        data = self.data
        purchase_return = PurchaseReturn.objects.create(
            purchase=data.purchase
        )
        purchase_return.save()
        book = data.purchase.book
        book.quantity -= data.purchase.quantity
        book.save()
        return purchase_return
