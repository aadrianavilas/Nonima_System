from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from payroll.forms.employees import EmployeeForm
from payroll.forms.sobre_tiempo import SobreTiempoForm
from payroll.models import Employee, Sobretiempo, TipoSobretiempo
from django.db.models import Q
from payroll.helpers.utilies import is_valid_dni, paginator
# Create your views here.


@login_required(login_url='sign_in')
def list_sobretiempo(request):
    try:
        query=request.GET.get('search',None)
        if query: 
            list_sobretiempo=Sobretiempo.objects.filter(Q(empleado__name__icontains=query))
        else: 
            list_sobretiempo=Sobretiempo.objects.all()
        print(list_sobretiempo)
        context=paginator(request,list_sobretiempo)

        return render(request,'sobretiempo/list_sobretiempo.html',context)
    except Exception:
        context['error']='Error al buscar'
        return render(request,'sobretiempo/list_sobretiempo.html',context)

@login_required(login_url='sign_in')
def create_sobretiempo(request):
    try:   
        if request.method=='GET':
            form=SobreTiempoForm()
            return render(request,'sobretiempo/create.html',{'form':form,'title':'Registrar sobretiempo'})

        form=SobreTiempoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payroll:list_sobretiempo')
        return render(request,'sobretiempo/create.html',{'form':form,'title':'Registrar sobretiempo','error':'Formulario llenado incorrectamente'})
        
    except Exception:
        return render(request,'sobretiempo/create.html',{'form':form,'title':'Registrar sobretiempo','error':'Error al guardar el sobretiempo'})
    

@login_required(login_url='sign_in')
def update_sobretiempo(request,id):
    try:
        sobretiempo=get_object_or_404(Sobretiempo,id=id)
        if request.method=='GET':
            form=SobreTiempoForm(instance=sobretiempo)
            return render(request,'sobretiempo/create.html',{'form':form,'title':'Actualizar sobretiempo'})


        form=SobreTiempoForm(request.POST,instance=sobretiempo)
        if form.is_valid():
            form.save()
            return redirect('payroll:list_sobretiempo')
        return render(request,'sobretiempo/create.html',{'form':form,'title':'Actualizar sobretiempo','error':'Formulario llenado incorrectamente'})
    
        
    except Exception:
        return render(request,'sobretiempo/create.html',{'form':form,'title':'Actualizar sobretiempo','error':'Error al guardar el sobretiempo'})
    

@login_required(login_url='sign_in')
def delete_sobretiempo(request,id):
    try:
        sobretiempo=get_object_or_404(Sobretiempo,id=id)
        if request.method=='GET':
            return render(request,'sobretiempo/delete.html',{'sobretiempo':sobretiempo,'title':'Eliminar sobretiempo'})

        sobretiempo.delete()
        return redirect('payroll:list_sobretiempo')

    except Exception:
        return render(request,'sobretiempo/delete.html',{'sobretiempo':sobretiempo,'error':'Error al eliminar el sobretiempo','title':'Eliminar sobretiempo'})


def get_tipo_sobretiempo_data(request,id_empleado,id_tipo_sobretiempo):
    try:
        tipo_sobretiempo = TipoSobretiempo.objects.get(id=id_tipo_sobretiempo)
        empleado = Employee.objects.get(id=id_empleado)
        return JsonResponse({
            'factor': str(tipo_sobretiempo.factor),
            'salario': str(empleado.salary),
            
        })
    except Employee.DoesNotExist:
        return JsonResponse({'error': 'no encontrado'}, status=404)