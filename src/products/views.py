from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm
from django.http import Http404

# Create your views here.

def product_list_view(request):
    queryset = Product.objects.all() # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)



def product_delete_view(request, my_id):
    obj =get_object_or_404(Product, id =my_id)
    # Need to confirm it's a POST request
    if request.method == 'POST':
        # confirm if the user wants to delete.
        obj.delete()
        return redirect('../../')
    context={
        "object" : obj
    }
    return render(request, "products/product_delete.html", context)

def dynamtic_lookup_view(request, my_id):
    # obj = Product.objects.get(id=my_id)
    # obj = get_object_or_404(Product, my_id)
    try:
        obj = Product.objects.get(id=my_id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "object" : obj
    }
    return render(request, "products/product_detail.html", context)


def product_create_view(request):
    myform = RawProductForm()
    if request.method == 'POST':
        myform = RawProductForm(request.POST)
        if myform.is_valid():
            # DJango가 user가 input한 데이터를 확인함.
            print(myform.cleaned_data)
            Product.objects.create(**myform.cleaned_data)
        else:
            print(myform.errors)
    context ={
        'form': myform
    }
    return render(request, "products/product_create.html", context)


# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm(request.POST or None) # 리셋시키기
#     context ={
#         'form' : form
#     }
#     return render(request, "products/product_create.html", context)




def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context ={
    #     'title' : obj.title
    # } # 이렇게 하는 것 보다 그냥 obj를 context로 보내는 것이 좋을 것.
    context ={
        'object' : obj
    }
    return render(request, "products/product_detail.html", context)
