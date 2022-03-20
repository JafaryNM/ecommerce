from pyexpat import model
from typing import List
from unicodedata import category
from django.shortcuts import render
from django.views.generic import ListView
from .models import *

# Create your views here.


class DisplayProducts(ListView):
    model=Product
    tempalate_name='store/home.html'
    category=Category.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(DisplayProducts, self).get_context_data(**kwargs)
        context['products']=Product.objects.all()
        context['categories']=self.category
        return context
    
    
