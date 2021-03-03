from django.db import models
from django.db.models import Q
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=100)
    primaryCategory = models.BooleanField(default=False)


    def __unicode__(self):
        return self.title

class Product(models.Model):
    image = models.ImageField(upload_to='products/')
    name = models.CharField(max_length=300)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    preview_text = models.TextField(max_length=200, verbose_name='Preview Text')
    detail_text = models.TextField(max_length=1000, verbose_name='Detail Text')
    price = models.FloatField()

    def __unicode__(self):
        return self.title


    #def save(self, *args, **kwargs):
     #   super(Product, self).save(*args, **kwargs)
      #  if self.variation_set.all().count() == 0:
       #     Variation.objects.create(
        #        product=self, price=self.price, title='Default')

class ProductFeatured(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')
    title = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.product.title
