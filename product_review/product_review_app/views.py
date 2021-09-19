from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, ProductReview
from django.template import loader
from django.urls import reverse


def index(request):
    product_review_list = ProductReview.objects.all()
    template = loader.get_template('review.html')
    context = {
        'product_review_list': product_review_list
    }
    return HttpResponse(template.render(context, request))


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

    return HttpResponse(reverse('product_review_app:index'))
