from django.shortcuts import render, redirect
from django.http import HttpResponseServerError
from .models import MyTable
from .forms import MyTableForm, SignUpForm, LoginForm
from .filters import FormFilter
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def signup(request):
    hide_signin = False
    if request.user.is_authenticated:
        return redirect('details')
    else:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, f'Hi {user}, Account Created Successfully. Use your credentials to login ')
                return redirect('signin')
        else:
            form = SignUpForm()
        return render(request, 'sign_up.html', {'form': form, 'hide_signin': hide_signin})

def signin(request):
    hide_signin = False
    if request.user.is_authenticated:
        return redirect('details')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password')
                user =  authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('details')
                else:
                    messages.info(request, ' Username or Password is Incorrect')
        else:
            form = LoginForm()
    return render(request, 'sign_in.html' , {'form':form, 'hide_signin': hide_signin})

def signout(request):
    logout(request)
    return redirect('signin')

@login_required(login_url='signin')
def details(request):
    try:
        details = MyTable.objects.all()
        filter = FormFilter(request.GET, queryset=details)
        details = filter.qs
        return render(request, 'details.html', {'details': details, 'filter': filter})
    except Exception as e:
        return HttpResponseServerError(f"An error occurred: {str(e)}")

@login_required(login_url='signin')
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

@login_required(login_url='signin')
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

@login_required(login_url='signin')
def delete(request, id):
    try:
        detail = MyTable.objects.get(id=id)
        detail.delete()
        return redirect('details')
    except MyTable.DoesNotExist:
        return HttpResponseServerError("Record not found.")
    except Exception as e:
        return HttpResponseServerError(f"An error occurred: {str(e)}")
