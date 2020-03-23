from django.shortcuts import render
from .models import Item
from django.views.generic import ListView, DetailView
from django.http import HttpResponse


# Create your views here.
class HomeView(ListView):
    model = Item
    template_name = 'products/home.html'
    context_object_name = 'products'  # name to be used to loop over all products


class ProductDetailView(DetailView):
    model = Item
    template_name = 'products/products.html'

def checkoutpage(request):
    return render(request, "accounts/check_out.html")