from django import forms
from PFP_app.models import Employee, PerformanceInput

class PerformanceInputForm(forms.ModelForm):
    # Set employee_list to None initially
    employee_list = None

    # Constructor for the PerformanceInputForm class
    def __init__(self, *args, **kwargs):
        # Get the employee_list argument from the keyword arguments
        self.employee_list = kwargs.pop('employee_list', None)
        # Call the superclass constructor
        super(PerformanceInputForm, self).__init__(*args, **kwargs)
        # If employee_list is not None
        if self.employee_list:
            # Update the choices for the 'employee' field to be a list of tuples of (employee_id, full_name)
            self.fields['employee'].choices = [(employee.employee_id, f"{employee.first_name} {employee.last_name}") for employee in self.employee_list]

    # Define the metadata for the form
    class Meta:
        # Use the PerformanceInput model for the form
        model = PerformanceInput
        # Define the fields to include in the form
        fields = ['employee', 'performance_rating', 'sales_amount']
