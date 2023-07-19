import datetime
import xlwt
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseServerError
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
        if request.user.is_superuser:
            details = MyTable.objects.all()
        else:
            details = MyTable.objects.filter(user=request.user)
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
                new_entry = form.save(commit=False)
                new_entry.user = request.user
                new_entry.save()
                return redirect('details')
        except Exception as e:
            return HttpResponseServerError(f"An error occurred: {str(e)}")
    return render(request, 'form.html', {'form': form})

@login_required(login_url='signin')
def edit(request, id):
    try:
        edit_detail = MyTable.objects.get(id=id)
        if not (edit_detail.user == request.user or request.user.is_superuser):
            return HttpResponseForbidden("You don't have permission to edit this record.")
        
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
        if not (detail.user == request.user or request.user.is_superuser):
            return HttpResponseForbidden("You don't have permission to delete this record.")
        
        detail.delete()
        return redirect('details')
    except MyTable.DoesNotExist:
        return HttpResponseServerError("Record not found.")
    except Exception as e:
        return HttpResponseServerError(f"An error occurred: {str(e)}")

def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Data_' + str(datetime.datetime.now()) + '.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Data')
    rownum = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    if request.user.is_superuser:
        columns = ['Client Name', 'Entry Date', 'Modified At', 'Contact Number', 'Vendor Name', 'Vendor Company', 'Rate', 'Currency', 'Contract Type', 'Status', 'Comments', 'User']

        for col_num in range(len(columns)):
            ws.write(rownum, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        rows = MyTable.objects.select_related('user').values_list('client_name', 'date', 'modified_at', 'contact_number', 'vendor_name', 'vendor_company', 'rate', 'currency', 'contract_type', 'status', 'comments', 'user__username')

        for row in rows:
            rownum += 1

            for col_num in range(len(row)):
                ws.write(rownum, col_num, str(row[col_num]), font_style)

    else:
        columns = ['Client Name', 'Entry Date', 'Modified At', 'Contact Number', 'Vendor Name', 'Vendor Company', 'Rate', 'Currency', 'Contract Type', 'Status', 'Comments']

        for col_num in range(len(columns)):
            ws.write(rownum, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        rows = MyTable.objects.filter(user=request.user).values_list('client_name', 'date', 'modified_at', 'contact_number', 'vendor_name', 'vendor_company', 'rate', 'currency', 'contract_type', 'status', 'comments')

        for row in rows:
            rownum += 1

            for col_num in range(len(row)):
                ws.write(rownum, col_num, str(row[col_num]), font_style)

    wb.save(response)

    return response
