from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Contact
from django.forms import widgets


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ("timestamp",)
        widgets = {
            "name": widgets.TextInput(attrs={"placeholder": "Full Name"}),
            "email": widgets.EmailInput(attrs={"placeholder": "Email Address"}),
            "message": widgets.Textarea(attrs={"placeholder": "Your Message"}),
        }