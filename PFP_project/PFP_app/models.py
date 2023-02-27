from django.db import models

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100, default='sales')
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class PerformanceInput(models.Model):
    input_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Input ID')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    performance_rating = models.CharField(max_length=255)
    sales_amount = models.DecimalField(max_digits=10, decimal_places=2)