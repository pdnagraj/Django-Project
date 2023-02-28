from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from PFP_app.models import Employee
from PFP_app.models import PerformanceInput
from PFP_app.forms import PerformanceInputForm

# Create your views here.

# Home view
def home_view(request, *args, **kwargs):
    return render(request, 'base.html')

# Employees list view
def Employees_List_view(request, *args, **kwargs):
    employee_list = Employee.objects.all()
    context = {'employee_list': employee_list}
    return render(request, 'Employees_List.html', context)

Employees_List_view.http_method_names = ['get'] # Specify HTTP method as GET

# Performance list view
def Performance_List_view(request, *args, **kwargs):
    performance_list = PerformanceInput.objects.all().select_related('employee')
    context = {'performance_list': performance_list}
    return render(request, 'Employee_Performance_List.html', context)

Performance_List_view.http_method_names = ['get'] # Specify HTTP method as GET

# Performance input view
def Performance_Input_view(request, *args, **kwargs):
    employee_list = Employee.objects.all()

    # If the request is a POST request, validate the form data and save it if valid
    if request.method == 'POST':
        form = PerformanceInputForm(request.POST, employee_list=employee_list)
        if form.is_valid():
            form.save()
            # Redirect to performance_list if form saved successfully
            return redirect('performance_list')
    else:
        # If the request is not a POST request, create an instance of PerformanceInputForm with the employee list as an argument
        form = PerformanceInputForm(employee_list=employee_list)

    # Add the form and employee_list to the context dictionary
    context = {'form': form, 'employee_list': employee_list}
    
    # Render the Employee_Performance_Input.html template with the context dictionary as the template context
    return render(request, 'Employee_Performance_Input.html', context)


Performance_Input_view.http_method_names = ['get', 'post'] # Specify HTTP methods as GET and POST


def Delete_Performance(request, performance_id):
    performance = get_object_or_404(PerformanceInput, input_id=performance_id)
    if request.method == 'DELETE':
        performance.delete()
        return JsonResponse({'success': True})
    else:
        return HttpResponseNotAllowed(['DELETE'])
        
Delete_Performance.http_method_names = ['delete'] # Specify HTTP method as DELETE


