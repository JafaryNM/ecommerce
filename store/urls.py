from django.urls import path

from .views import *

app_name='store'

urlpatterns = [
    path('' , DisplayProducts.as_view(), name='viewallproducts')
]