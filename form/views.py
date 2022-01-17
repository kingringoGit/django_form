from django.shortcuts import render,redirect
from .forms import Employee_form
from .models import Employee
# Create your views here.

# def display_form(request):
#     form=Employee_form()
#     return render(request,'index.html',{'f1':form})
def save_fun(request):
    if request.method=="POST":
        data=Employee_form(request.POST)
        if data.is_valid():
            data.save()
        return redirect('/dispdata')
    else:
        form = Employee_form()
        return render(request, 'index.html', {'f1': form})
def fetch_all(request):
    data=Employee.objects.all()
    return render(request,'show.html',{'res':data})
def edit_fun(request,id):
    spec_data= Employee.objects.get(id=id)
    return render(request,'edit.html',{'res':spec_data})
def update_fun(request,id):
    spec_data = Employee.objects.get(id=id)
    if request.method=="POST":
        data=Employee_form(request.POST,instance=spec_data)
        if data.is_valid():
            data.save()
        return redirect('/dispdata')
    else:
        form = Employee_form()
        return render(request, 'index.html', {'f1': form})
def delete_fun(request,id):
    spec_data = Employee.objects.get(id=id)
    spec_data.delete()
    data = Employee.objects.all()
    return render(request, 'show.html', {'res': data})

# def detail(request,ename):
#     spec_data = Employee.objects.filter(ename=ename)
#     return render(request,'detail.html',{'res':spec_data})





