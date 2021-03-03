#import random

#from django.contrib import messages
#from django.http import Http404
#from django.shortcuts import render, get_object_or_404, redirect
#from django.views.generic.detail import DetailView
from django.views.generic import ListView
#from django.db.models import Q

from products.models import Product

# Create your views here.

class Home(ListView):
    model = Product
    template_name = 'products/home.html'