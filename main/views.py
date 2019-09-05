from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.forms import UserCreationForm




def homepage(request):
    return render(request=request,
                  template_name = "home.html",
                  context = {"products": Product.objects.all})
                  

def register(request):
    form = UserCreationForm
    return render(request,
                  "register.html",
                  context = {"form": form}
                  )