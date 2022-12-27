from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')

def show_catalog(request):
    template = 'catalog.html' 
    phone_objects = Phone.objects.all()
    sort = request.GET.get('sort')
    if sort == 'name':
        phones = phone_objects.order_by('name')
    elif sort == 'min_price':
        phones = phone_objects.order_by('price')
    elif sort == 'max_price':
        phones = phone_objects.order_by('-price')
    else:
        phones = phone_objects
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
        context = {'phone': phone}
    return render(request, template, context)



  
    
    
   
