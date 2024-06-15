from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.urls import reverse_lazy

from main.models import Product
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def root(request):
    return redirect("products_list")


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
