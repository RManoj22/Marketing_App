from django.shortcuts import render, redirect
from .models import MyTable
from .forms import MyTableForm

# Create your views here.

def details(request):
    details = MyTable.objects.all()
    return render(request,'details.html',{'details':details})

def addnew(request):
    form = MyTableForm()
    if request.method =='POST':
        form = MyTableForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/table')
    return render(request,'form.html',{'form':form})

def edit(request,id):
    edit_detail = MyTable.objects.get(id=id)
    form = MyTableForm(request.POST,instance=edit_detail)
    if form.is_valid():
        form.save()
        return redirect('/table')
    return render(request,'edit.html',{'edit_detail':edit_detail})

def delete(request,id):
    detail = MyTable.objects.get(id=id)
    detail.delete()
    return redirect('/table')
