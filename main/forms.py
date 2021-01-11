from django import forms
from .models import Stock
from django.forms import ModelForm


class SearchQuote(forms.Form):
    ticker = forms.CharField(
        label="",
        max_length=200,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Try: AAPL"}
        ),
    )


class BuyForm(forms.Form):
    ticker = forms.CharField(
        label="Ticker",
        max_length=200,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Try: AAPL"}
        ),
    )
    shares = forms.IntegerField(
        label="Shares",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Try: 10"}
        ),
    )
