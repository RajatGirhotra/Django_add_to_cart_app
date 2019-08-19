from django.db import models
from datetime import datetime

# Create your models here.
class Product(models.Model):
    product_title = models.CharField(max_length=200)
    product_content = models.TextField()
    product_published = models.DateTimeField("date published", default= datetime.now)
    
    def __str__(self):
        return self.product_title
    

