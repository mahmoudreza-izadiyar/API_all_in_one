from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.IntegerField()
    date_of_exp = models.DateField()
    available = models.BooleanField()

    def __str__(self):
        return self.title
