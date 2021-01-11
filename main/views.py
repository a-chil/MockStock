from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import finnhub
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import SearchQuote, BuyForm
from django.utils import timezone

finnhub_client = finnhub.Client(api_key="bvpnicf48v6rjmkhujgg")

# Create your views here.
def home(request):

    username = request.user.username

    quote = {}
    company = {}
    ticker = ""
    ETF = {}

    # popular ETF header Carousel
    pop_ETF = {
        "SPY": {
            "etf_profile": (finnhub_client.etfs_profile("SPY")),
            "quote": finnhub_client.quote("SPY"),
        },
        "VOO": {
            "etf_profile": (finnhub_client.etfs_profile("VOO")),
            "quote": finnhub_client.quote("VOO"),
        },
        "QQQ": {
            "etf_profile": (finnhub_client.etfs_profile("QQQ")),
            "quote": finnhub_client.quote("QQQ"),
        },
        "GLD": {
            "etf_profile": (finnhub_client.etfs_profile("GLD")),
            "quote": finnhub_client.quote("GLD"),
        },
        "IWM": {
            "etf_profile": (finnhub_client.etfs_profile("IWM")),
            "quote": finnhub_client.quote("IWM"),
        },
        "XLF": {
            "etf_profile": (finnhub_client.etfs_profile("XLF")),
            "quote": finnhub_client.quote("XLF"),
        },
    }

    if request.method == "POST":
        form = SearchQuote(request.POST)

        if form.is_valid():
            ticker = form.cleaned_data["ticker"].upper()
            company = finnhub_client.company_profile2(symbol=ticker)
            quote = finnhub_client.quote(ticker)
            ETF = finnhub_client.etfs_profile(ticker)

    else:
        form = SearchQuote()

    my_dict = {
        "form": form,
        "quote": quote,
        "company": company,
        "ticker": ticker,
        "ETF": ETF,
        "pop_ETF": pop_ETF,
        "username": username,
    }
    return render(request, "main/home.html", my_dict)


@login_required(login_url="/login")
def portfolio(request):
    current_user = request.user
    username = current_user.username
    profile = current_user.profile

    stocks = current_user.profile.stock_set.all()

    curr_price = {}
    for curr_stock in stocks:
        curr_price[curr_stock] = finnhub_client.quote(curr_stock.symbol)

    if request.method == "POST":
        form = BuyForm(request.POST)
        if form.is_valid():
            ticker = form.cleaned_data["ticker"].upper()
            company = finnhub_client.company_profile2(symbol=ticker)
            shares = form.cleaned_data["shares"]
            quote = finnhub_client.quote(ticker)
            if bool(company):
                s = Stock.objects.create(
                    user=profile,
                    name=company["name"],
                    symbol=company["ticker"],
                    price_per_stock=quote["c"],
                    shares=shares,
                    purchase_date=timezone.now(),
                )
                s.save()
            return redirect("/portfolio")
    else:
        form = BuyForm()

    my_dict = {
        "username": username,
        "form": form,
        "stocks": stocks,
        "user": current_user,
        "curr_price": curr_price,
    }
    return render(request, "main/portfolio.html", my_dict)


@login_required
def deleteStock(request, pk):
    stock = Stock.objects.get(id=pk)
    profile = request.user.profile

    if profile == stock.user:
        stock.delete()
        return redirect("/portfolio")
    else:
        return redirect("/portfolio")

    return render(
        request,
    )


def aboutView(request):
    return render(request, "main/about.html")
