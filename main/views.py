from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from main.models import Products


# Create your views here.
def products_list(request):
    products_list = Products.objects.all()
    template = loader.get_template("main/products_list.html")
    context = {
        "products_list": products_list
    }

    return HttpResponse(template.render(context, request))


def product_page(request):
    return HttpResponse("<h2>Product page</h2>")


def cart(request):
    return HttpResponse("<h2>Shopping cart</h2>")