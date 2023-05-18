from django.db.models import Q
from django.shortcuts import render
from .models import Product,Category
def search(request):
    query=request.GET.get('query','')
    products=Product.objects.filter(Q(title__icontains=query)|Q(description__icontains=query))
    return render(request,'store/search.html',{'query':query,'products':products})
def product_detail(request,category_slug,slug):
    product=Product.objects.get(slug=slug)
    return render(request,'store/product_detail.html',{'product':product})
def category_detail(request,slug):
    category=Category.objects.get(slug=slug)
    products=category.products.all()
    return render(request,'store/category_detail.html',{'category':category,'products':products}) 