from django.shortcuts import render
from django.http import HttpResponse
from .models import Product




def homepage(request):
    return render(request=request,
                  template_name = "home.html",
                  context = {"products": Product.objects.all})