from django import forms
from .models import Sale, Purchase


class SaleForm(forms.ModelForm):
    class Meta(object):
        model = Sale
        fields = ["book", "quantity", "customer", "remarks",]
        help_texts = {
            "book": "Choose Book",
            "quantity": "Enter Sale Quantity",
            "customer": "Enter purchasing quantity",
            "remarks": "Enter remarks"
        }


class PurchaseForm(forms.ModelForm):
    class Meta(object):
        model = Purchase
        fields = ["book", "quantity", "whole_seller", "remarks",]
        help_texts = {
            "book": "Choose Book",
            "quantity": "Enter Purchase Quantity",
            "whole_seller": "Enter Wholeseller",
            "remarks": "Enter remarks"
        }
