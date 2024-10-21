from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=32)

    def __str__(self):
        return str(self.category_name)


class Product(models.Model):
    product_name = models.CharField(max_length=128)
    product_description = models.TextField()
    product_photo = models.ImageField(upload_to='media')
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product_name)