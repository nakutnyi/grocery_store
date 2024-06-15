from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from main.models import Product


def root(request):
    return redirect("products_list")

# Create your views here.
def products_list(request):
    products_list = Product.objects.all()
    template = loader.get_template("products_list.html")
    context = {
        "products_list": products_list
    }

    return HttpResponse(template.render(context, request))


def product_page(request):
    return HttpResponse("<h2>Product page</h2>")


def cart(request):
    return HttpResponse("<h2>Shopping cart</h2>")


def login(request):
    return HttpResponse("<h2>Login page</h2>")


def user_settings(request):
    return HttpResponse("<h2>User settings</h2>")
