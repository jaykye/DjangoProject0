from django.shortcuts import render
from .models import Product
from .forms import ProductForm

# Create your views here.


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm(request.POST or None) # 리셋시키기
    context ={
        'form' : form
    }
    return render(request, "products/product_create.html", context)




def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context ={
    #     'title' : obj.title
    # } # 이렇게 하는 것 보다 그냥 obj를 context로 보내는 것이 좋을 것.
    context ={
        'object' : obj
    }
    return render(request, "products/product_detail.html", context)
