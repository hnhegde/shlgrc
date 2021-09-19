from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, ProductReview


def index(request):
    return render(request, 'review.html')


def review(request, product_id):
    print(request.body)
    print("product id: ", product_id)
    if request.method == 'POST':
        ProductReview.objects.create(
            product_id=Product.objects.get(pk=product_id),
            review=request.POST.get('reviewText', None),
            rating=request.POST.get('ratedStars', None)
        )
    else:
        print(request.method)

    return HttpResponse("review submitted.")
