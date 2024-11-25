# main/forms.py
from django import forms
from .models import ReviewSite, Contact, BookRental


class BookRentalForm(forms.ModelForm):
    class Meta:
        model = BookRental
        fields = ['name', 'email', 'message']

class ReviewSiteForm(forms.ModelForm):
    class Meta:
        model = ReviewSite
        fields = ['name', 'comment', 'rating']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
