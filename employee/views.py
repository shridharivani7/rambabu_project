from django.shortcuts import render,redirect
from employee.forms import EmployeeForm  
from employee.models import Emp  
# Create your views here.
import pdb
def emp(request):  
    pdb.set_trace()
    if request.method == "POST":  
        #pdb.set_trace()
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                #return True
                return redirect('/show')  
            except:  
                pass  
    else:
        #pdb.set_trace()
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  

def show(request):  
    employees = Emp.objects.all()  
    #pdb.set_trace()
    return render(request,"show.html",{'employees':employees,}) 

def edit(request, id):  
    employee = Emp.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
