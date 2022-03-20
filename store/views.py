from pyexpat import model
from typing import List
from django.shortcuts import render
from django.views.generic import ListView
from .models import *

# Create your views here.


class DisplayProducts(ListView):
    model=Product
    tempalate_name='store/home.html'
    
