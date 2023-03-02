from django.urls import path
from PFP_app import views
from PFP_app.views import Employees_List_view
from PFP_app.views import Performance_List_view
from PFP_app.views import Performance_Input_view 
from PFP_app.views import Delete_Performance 


urlpatterns = [
    path('', views.home_view, name='home'),
    path('employees/', Employees_List_view, name='employee_list'),
    path('employees_performance_list/', Performance_List_view, name='performance_list'),
    path('employees_performance_input_form/', Performance_Input_view, name='performance_input_form'),
    path('delete_performance/<int:performance_id>/', Delete_Performance, name='delete_performance'),
]
