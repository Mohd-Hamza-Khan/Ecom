from django.urls import path
from products.views import show_prod

urlpatterns = [
    # path('<slug>/' , get_product , name="get_product"),
    path('show_prod/' , show_prod , name="show_prod"),
]
