from django.shortcuts import render, Http404
from .models import Product
from marketing.models import MarketingMessage, Slider


def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        products = Product.objects.filter(title__icontains=q)
        context = {"query": q, "products": products}
        template = 'products/results.html'
    else:
        context = {}
        template = 'products/home.html'
    return render(request, template, context)


def home(request):
    sliders = Slider.objects.all()
    products = Product.objects.all()
    marketing_message = MarketingMessage.objects.get_featured_item()
    context = {'products': products, 'sliders': sliders}
    template = 'products/home.html'
    return render(request, template, context)


def all(request):
    products = Product.objects.all()
    context = {'products': products}
    template = 'products/all.html'
    return render(request, template, context)

def single(request, slug):
    product = Product.objects.get(slug=slug)  # If there is not any product it will throw HTTP 404 error
    images = product.productimage_set.all()
    context = {'product': product, 'images': images}
    template = 'products/single.html'
    return render(request, template, context)
    # try:
    #     product = Product.objects.get(slug=slug)  #If there is not any product it will throw HTTP 404 error
    #     images = product.productimage_set.all()
    #     context = {'product': product, 'images': images}
    #     template = 'products/single.html'
    #     return render(request, template, context)
    # except:
    #     raise Http404