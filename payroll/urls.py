from django.urls import path
from payroll.views import auth, contract_type, department,employees,payslip,position, sobretiempo


app_name='payroll'
urlpatterns = [ 
    path('sign/out/',auth.sign_out,name='sign_out'),
    path('dashboard/',auth.dashboard,name='dashboard'),

    path('list/employees/',employees.list_employee,name='list_employees'),
    path('create/employee/',employees.create_employee,name='create_employee'),
    path('update/employee/<int:id>/',employees.update_employee,name='update_employee'),
    path('delete/employee/<int:id>/',employees.delete_employee,name='delete_employee'),

    path('create_position/',position.create_position,name='create_position'),
    path('list_positions/',position.list_positions,name='list_positions'),
    path('update_position/<int:id>/',position.update_position,name='update_position'),
    path('delete_position/<int:id>/',position.delete_position,name='delete_position'),

    path('list/payslips/', payslip.list_payslip, name='list_payslip'),
    path('create/payslip/', payslip.create_payslip, name='create_payslip'),
    path('update/payslip/<int:id>/', payslip.update_payslip, name='update_payslip'),
    path('delete/payslip/<int:id>', payslip.delete_payslip, name='delete_payslip'),

    path('list/contract/type/', contract_type.list_contract_type, name='list_contract_types'),
    path('create/contract/type/', contract_type.create_contract_type, name='create_contract_type'),
    path('update/contract/type/<int:id>/', contract_type.update_contract_type, name='update_contract_type'),
    path('delete/contract/type/<int:id>', contract_type.delete_contract_type, name='delete_contract_type'),

    path('list/department/', department.list_department, name='list_departments'),
    path('create/department/', department.create_department, name='create_department'),
    path('update/department/<int:id>/', department.update_department, name='update_department'),
    path('delete/department/<int:id>', department.delete_department, name='delete_department'),

    path('list/sobretiempo/', sobretiempo.list_sobretiempo, name='list_sobretiempo'),
    path('create/sobretiempo/', sobretiempo.create_sobretiempo, name='create_sobretiempo'),
    path('update/sobretiempo/<int:id>/', sobretiempo.update_sobretiempo, name='update_sobretiempo'),
    path('delete/sobretiempo/<int:id>', sobretiempo.delete_sobretiempo, name='delete_sobretiempo'),


   
]