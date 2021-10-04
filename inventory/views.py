from django.shortcuts import render
from .models import Desktop,Laptop,Mobile
from .forms import *
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.

def index(request):
    return render(request,'inventory/index.html')
def display_laptop(request):
    items=Laptop.objects.all()
    return render(request,'inventory/index.html',{'items':items,'header':'Laptops'})


def display_mobile(request):
    items=Mobile.objects.all()
    return render(request,'inventory/index.html',{'items':items,'header':'Mobiles'})

def display_desktop(request):
    items=Desktop.objects.all()
    return render(request,'inventory/index.html',{'items':items,'header':'Desktops',})


def add_Device(request,fun,model):
    if request.method=='POST':
        form=fun(request.POST)
        if form.is_valid():
            type=form.cleaned_data['type']
            price=form.cleaned_data['price']
            status=form.cleaned_data['status']
            Quantity=form.cleaned_data['Quantity']
            obj=model(type=type,price=price,status=status,Quantity=Quantity)
            obj.save()
        return HttpResponseRedirect('/')
    else:
        form=fun()
        return render(request,'inventory/add_new.html',{'form':form})

def add_mobile(request):
    return add_Device(request,MobileForm,Mobile)

def add_laptop(request):
    return add_Device(request,LaptopForm,Laptop)

def add_desktop(request):
    return add_Device(request,DesktopForm,Desktop)

def edit_device(request,id,model,fun):
    item=model.objects.get(pk=id)
    if request.method=="POST":
        form=fun(request.POST,instance=item)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    else:
        form=fun(instance=item)
        return render(request,'inventory/edit_item.html',{"form":form})
def edit_mobile(request,id):
    return edit_device(request,id,Mobile,MobileForm)

def edit_laptop(request,id):
    return edit_device(request,id,Laptop,LaptopForm)

def edit_desktop(request,id):
    return edit_device(request,id,Desktop,DesktopForm)



def delete_device(request,id,model):
    model.objects.get(pk=id).delete()
    return HttpResponseRedirect('/')
    


def delete_mobile(request,id):
    return delete_device(request,id,Mobile)

def delete_laptop(request,id):
    return delete_device(request,id,Laptop)

def delete_desktop(request,id):
    return delete_device(request,id,Desktop)


def about(request):
    return render(request,'inventory/about.html')


def contact(request):
    if request.method=="POST":
        return render(request,'inventory/index.html')
    else:
        return render(request,'inventory/contact.html')

def search(request):
    if request.method=='GET':
        product=''
        MODEL=''
        p_name=request.GET['p_name'].strip()
        objs1=Mobile.objects.filter(type__icontains=p_name)
        objs2=Laptop.objects.filter(type__icontains=p_name)
        objs3=Desktop.objects.filter(type__icontains=p_name)
        if objs1:
            MODEL='mobile'
            product=objs1
        elif objs2:
            MODEL='laptop'
            product=objs2
        elif objs3:
            MODEL='desktop'
            product=objs3
        else:
            product='null'
            return render(request,'inventory/index.html',{'product':product,'p_name':p_name})
        return render(request,'inventory/search.html',{'product':product,'header':MODEL})
    






