from pydoc import render_doc
from tkinter import E
from django.shortcuts import render
from products.models import Product




# def get_product(request , slug):
#     try:
#         product = Product.objects.get(slug =slug)
#         context = {'product' : product}
#         return render(request  , 'product/product.html' , context)

#     except Exception as e:
#         print(e)
        

def show_prod(request):
    product = Product.objects.all()
    context = {'product' : product}
    return render(request  , 'show_product.html' , context)
    