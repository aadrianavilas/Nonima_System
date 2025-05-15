from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator

# Create your models here.
class Position(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class Department(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description



class ContractType(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description



class Employee(models.Model):
    SEX_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ]
    name = models.CharField(max_length=100)
    dni = models.CharField(max_length=10, unique=True)
    address = models.TextField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    salary = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    contract_type = models.ForeignKey(ContractType,on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Payslip(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    year_month = models.IntegerField()#202501
    salary = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    overtime_hours = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    bonus = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    
    #calculado
    iess = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    tot_ing = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    tot_des = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    neto = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])

    def __str__(self):
        return self.employee.name

    def calculate_tot_ing(self):
        self.tot_ing=self.salary+self.overtime_hours+self.bonus

    def calculate_iess(self):
        self.iess=self.salary*Decimal('0.0945')

    def calculate_neto(self):
        self.neto=self.tot_ing-self.tot_des

    def get_year_month_display(self):
        year = self.year_month // 100
        month = self.year_month % 100
        return f"{year}-{month:02d}"

    def save(self,*args,**kgars):
        self.calculate_tot_ing()
        self.calculate_iess()
        self.tot_des=self.iess
        self.calculate_neto()

        super().save(*args,**kgars) #guardar en la base de datos con los campos calculados


class TipoSobretiempo(models.Model):
    descripcion = models.CharField(max_length=100)
    factor = models.DecimalField(max_digits=3, decimal_places=2)
    
    def __str__(self):
        return f"{self.descripcion} (Factor: {self.factor})"
    

class Sobretiempo(models.Model):
    empleado = models.ForeignKey(Employee, on_delete=models.CASCADE)
    tipo_sobretiempo = models.ForeignKey(TipoSobretiempo, on_delete=models.CASCADE)
    fecha_sobretiempo = models.DateField()
    numero_horas = models.DecimalField(max_digits=5, decimal_places=2,validators=[MinValueValidator(1)])
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    
       
    def __str__(self):
        return f"Sobretiempo de {self.empleado.name} - {self.fecha_sobretiempo}"
    

    def show_active(self):
        return  'Activo' if self.is_active else 'Inactivo'