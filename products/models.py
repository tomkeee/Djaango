from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title       =models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=9,default=0.0)
    summary = models.TextField(blank=False, null=False,default="empty")  # null=True, default=True

    def get_absolute_url(self):
        return reverse("product:product-details",kwargs={"id":self.id})
