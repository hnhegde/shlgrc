from django.contrib import admin
from .models import Product, ProductReview

admin.site.register(Product)

# Remove this for final delivery. Required during development only
admin.site.register(ProductReview)
