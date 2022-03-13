
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
   name=models.CharField(max_length=200, db_index=True, null=True,blank=True )
   slug=models.SlugField(max_length=100, unique=True)
   
   class  Meta:
     verbose_name_plural = 'Categories'
     def __str__(self):
         return self.name
     

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='Product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='ProductCreator', on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length = 150)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    instock=models.BooleanField(default=True)
    isactive=models.BooleanField(default=True)
    created_date=models.DateField(auto_now_add='True')
    update_date=models.DateField(auto_now=True)
    
    class  Meta:
        verbose_name_plural = 'Products'
        ordering=('-created_date',)
    
    def __str__(self):
        return self.title
    
    
    
    