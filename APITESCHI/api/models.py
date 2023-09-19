from django.db import models

# Create your models here.


class clientes(models.Model):
    idClientes = models.IntegerField(primary_key=True, db_column='idClientes')
    Nombre = models.CharField(max_length=100,db_column='Nombre')
    Apellido = models.CharField(max_length=100, db_column='Apellido')
    Correo_Electronico = models.EmailField(max_length=100, db_column='Correo Electronico')
    Telefono = models.IntegerField(db_column= 'Telefono')
    class Meta:
        db_table = 'clientes'
        
class direccion (models.Model):
    idDireccion = models.IntegerField(primary_key=True, db_column='idDireccion')
    colonia =  models.CharField(max_length=100,db_column='colonia')
    ciudad =  models.CharField(max_length=100,db_column='ciudad')
    Municipio =  models.CharField(max_length=100,db_column='Municipio')
    Estado =  models.CharField(max_length=100,db_column='Estado')
    COdigoPostal =  models.CharField(max_length=100,db_column='COdigoPostal')
    class Meta:
        db_table = 'direccion'

class EtiquetaCliente (models.Model):
    idEtiquetaCliente = models.IntegerField(primary_key=True, db_column='idEtiquetaCliente')
    etiqueta = models.CharField(unique=True,max_length=100, db_column='etiqueta')
    class Meta:
        db_table = 'EtiquetaCliente'
        
class Estado (models.Model):
    idEstado = models.IntegerField(primary_key=True, db_column='idEstado')
    estado = models.CharField(unique=True,max_length=100, db_column='estado')
    class Meta:
        db_table = 'Estado'

class Actividades_Compra (models.Model):
    idActvidadesCliente = models.IntegerField(primary_key=True, db_column='idActvidadesCliente')
    categoria = models.CharField(unique=True,max_length=100, db_column='categoria')
    class Meta:
        db_table = 'Actividades_Compra'

class Nota (models.Model):
    idNota = models.IntegerField(primary_key=True, db_column='idNota')
    Fecha = models.DateField (db_column='Fecha')
    Nota = models.CharField(max_length=1000, db_column='categoria')
    FKidClientes = models.ForeignKey(clientes, on_delete=models.CASCADE,db_column='FKidClientes')
    class Meta:
        db_table = 'Nota'

class InteraccionCliente (models.Model):
    idInteCliente = models.IntegerField(primary_key=True, db_column='idInteCliente')
    FKidClientes = models.ForeignKey(clientes, on_delete=models.CASCADE,db_column='FKidClientes')
    Fecha = models.DateField (db_column='Fecha')
    FKEtiquetaCliente = models.ForeignKey(EtiquetaCliente, on_delete=models.CASCADE,db_column='FKEtiquetaCliente')
    class Meta:
        db_table = 'InteraccionCliente'
    
class Compra  (models.Model):
     idActividades = models.IntegerField(primary_key=True, db_column='idActividades')
     FKActividades_Compra = models.ForeignKey(Actividades_Compra, on_delete=models.CASCADE,db_column='Actividades_Compra')
     Fecha = models.DateField (db_column='Fecha')
     FKclientes = models.ForeignKey(clientes, on_delete=models.CASCADE,db_column='FKclientes')
     FKEstado = models.ForeignKey(Estado, on_delete=models.CASCADE,db_column='FKEstado')
     class Meta:
        db_table = 'Compra'
        
class Direccion_Clientes (models.Model):
    idDireccion_Clientes  = models.IntegerField(primary_key=True, db_column='Direccion_Clientes')
    FKidDireccion = models.ForeignKey(direccion, on_delete=models.CASCADE,db_column='FKidDireccion')
    FKclientes = models.ForeignKey(clientes, on_delete=models.CASCADE,db_column='FKclientes')