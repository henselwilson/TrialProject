from django.shortcuts import render,redirect
from .forms import Phone_form, Phone_edit_form
from .models import Phone

# Create your views here.
def home_view(request):
    return render(request,'index.html')

def Phone_input_view(request):
    if request.method=='POST':
        form=Phone_form((request.POST))
        if form.is_valid():
            form.save()
            return redirect('/createPhone')
    else:
        form=Phone_form
    context={
    'form':form
    }
    return render(request,'addPhone.html',context)

def Phone_list_view(request):
    if request.method=='GET':
        result=Phone.objects.all()
        context={
            'result':result
        }
        return render(request,'PhoneResult.html',context)

def Phone_edit_view(request,id):
    instance = Phone.objects.filter(id=id).first()
    form = Phone_edit_form(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
    context={
        'form':form
    }
    return render(request,'EditPhone.html',context)

#def make_order(request):