from django.shortcuts import render, redirect
from django.http import HttpResponseServerError
from .models import MyTable
from .forms import MyTableForm, SignUpForm
from .filters import FormFilter 

def signup(request):
    form = SignUpForm(request.POST)
    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                return redirect('signup_success')
        except Exception as e:
            return HttpResponseServerError(f"An error occurred: {str(e)}")
    return render(request, 'sign_up.html', {'form': form})

def signin(request):
    return render(request, 'sign_in.html')

def details(request):
    try:
        details = MyTable.objects.all()
        filter = FormFilter(request.GET, queryset=details)
        details = filter.qs
        return render(request, 'details.html', {'details': details, 'filter': filter})
    except Exception as e:
        return HttpResponseServerError(f"An error occurred: {str(e)}")

def addnew(request):
    form = MyTableForm()
    if request.method == 'POST':
        try:
            form = MyTableForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('details')
        except Exception as e:
            return HttpResponseServerError(f"An error occurred: {str(e)}")
    return render(request, 'form.html', {'form': form})

def edit(request, id):
    try:
        edit_detail = MyTable.objects.get(id=id)
        contract_type = edit_detail.contract_type
        if request.method == 'POST':
            form = MyTableForm(request.POST, instance=edit_detail)
            if form.is_valid():
                form.save()
                return redirect('details')
        else:
            form = MyTableForm(instance=edit_detail)
        return render(request, 'edit.html', {'edit_detail': edit_detail, 'contract_type': contract_type, 'form': form})
    except MyTable.DoesNotExist:
        return HttpResponseServerError("Record not found.")
    except Exception as e:
        return HttpResponseServerError(f"An error occurred: {str(e)}")

def delete(request, id):
    try:
        detail = MyTable.objects.get(id=id)
        detail.delete()
        return redirect('details')
    except MyTable.DoesNotExist:
        return HttpResponseServerError("Record not found.")
    except Exception as e:
        return HttpResponseServerError(f"An error occurred: {str(e)}")
