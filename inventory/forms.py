from django import forms
from django.forms import widgets
from .models import Desktop,Mobile,Laptop
class DesktopForm(forms.ModelForm):
    class Meta:
        model=Desktop
        fields=('type','price','status','Quantity')
        labels={'type':'Product Name:','price':'Price:','status':'Availability:','Quantity':'Quantity:'}
        widgets={
            'type':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-select'}),
            'Quantity':forms.NumberInput(attrs={'class':'form-control'})

            }


class MobileForm(forms.ModelForm):
    class Meta:
        model=Mobile
        fields=('type','price','status','Quantity')
        labels={'type':'Product Name:','price':'Price:','status':'Availability:','Quantity':'Quantity:'}
        widgets={
            'type':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-select form-select-sm '}),
            'Quantity':forms.NumberInput(attrs={'class':'form-control'})

            }
        


class LaptopForm(forms.ModelForm):
    class Meta:
        model=Laptop
        fields=('type','price','status','Quantity')
        labels={'type':'Product Name:','price':'Price:','status':'Availability:','Quantity':'Quantity:'}
        widgets={
            'type':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-select'}),
            'Quantity':forms.NumberInput(attrs={'class':'form-control'})

            }



