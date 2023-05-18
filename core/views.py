from django.shortcuts import render
from store.models import Product
def frontpage(request):
    products = Product.objects.all()[0:10]
    return render(request,'core/frontpage.html',{'products':products})
def about(request):
    return render(request,'core/about.html')
