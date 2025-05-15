

from django import forms
from payroll.models import Sobretiempo


class SobreTiempoForm(forms.ModelForm):
    class Meta:
        model=Sobretiempo
        fields='__all__'
        # labels={
        #     'name':'Nombre',
        #     'dni':'Cédula',
        #     'address':'Dirección',
        #     'sex':'sexo',
        #     'salary':'Salario',
        #     'position':'Cargo',
        #     'department':'Departamento',
        #     'contract_type':'Tipo de contrato'
        # }
        widgets = {
            'empleado': forms.Select(attrs={'class': 'form-control'}),
            'tipo_sobretiempo': forms.Select(attrs={'class': 'form-control'}),
            'fecha_sobretiempo': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'},format='%Y-%m-%d'),
            'numero_horas': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            
        }