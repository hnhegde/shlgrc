from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.CharField(max_length=2000)


class ProductReview(models.Model):
    product_id = models.ForeignKey(Product, null=False, blank=False, on_delete=models.DO_NOTHING)
    rating = models.PositiveSmallIntegerField(null=False, blank=False)
    review = models.TextField(null=True, blank=True)
