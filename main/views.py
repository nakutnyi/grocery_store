from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.
def products_list(request):
    products_list = [
        "apple",
        "potato",
        "cranberries",
        "tomato",
        "banana",
    ]
    demo_string = "test"
    template = loader.get_template("main/templates/main/products_list.html")
    context = {
        "template_variable_name": demo_string,
    }

    return HttpResponse(template.render(context, request))


def product_page(request):
    return HttpResponse("<h2>Product page</h2>")


def cart(request):
    return HttpResponse("<h2>Shopping cart</h2>")