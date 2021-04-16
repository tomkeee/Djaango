from django.shortcuts import render, get_object_or_404,redirect
from django.http import Http404

from .forms import RawProductForm
from .models import Product

def product_create_view(request):
    form=RawProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=RawProductForm()
    context={
        'form':form
    }
    return render(request,"product_templates/product_create.html",context)


def dynamic_lookup_view(request,id):
    try:
        obj=Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    context={ "object":obj }
    return render(request,"product_templates/detail.html",context)

def delete_my_object(request,id):
    obj=Product.objects.get(id=id)
    if request.method=="POST":
        obj.delete()
        return redirect("success")
    context={
        "object":obj
    }
    return render(request,"product_templates/product_delete.html",context)

def delete_suc(request):
    obj=Product.objects.get()
    context={
        "object":obj
    }
    return render(request,"product_templates/product_delete_suc.html",context)

def product_list_view(request):
    queryset=Product.objects.all()
    context = {
        "object_list":queryset
    }
    return render(request,"product_templates/product_list.html",context)