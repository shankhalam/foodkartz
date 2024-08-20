from django.db import models

# Create your models here.

class items(models.Model):
    def __str__(self):
        return self.item_name
    
    item_name = models.CharField(max_length=50)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://alllocal.ca/wp-content/uploads/2020/11/food-placeholder.png")
