from django.db import models

# Create your models here.
#https://stackoverflow.com/questions/74600909/how-to-show-avaliable-sizes-of-clothes-on-the-form-django
class Category(models.model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name



class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    brand = models.CharField(max_length=200, ddefault="un-brabded")
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=250, unique=True)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    image = models.FileField(upload_to='images/', default="default.png")

    class Meta:
        verbose_name_plural = "products"

    def __str__(self):
        return self.title