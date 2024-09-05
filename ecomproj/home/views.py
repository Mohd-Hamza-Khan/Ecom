        

from django.shortcuts import render
from products.models import Product

# Create your views here.
def home(request):
    context = {'products' : Product.objects.all()}
    return render(request, 'home.html',context)

def hp15spage(request):
    return render(request, 'product/hp15spage.html')

def iphinepage(request):
    return render(request, 'product/iphinepage.html')

def macbookpage(request):
    return render(request, 'product/macbookpage.html')

def Rogphone7(request):
    return render(request, 'product/Rogphone7.html')

def samsungM1(request):
    return render(request, 'product/samsungM1.html')

def page(request):
    return render(request, 'product/page.html')
