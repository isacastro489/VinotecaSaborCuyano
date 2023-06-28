from dataclasses import dataclass,asdict,astuple, field
from typing import List, ClassVar, Any
from datetime import datetime,time,date
import validaciones.validar as validar

@dataclass (order=True)
class Proveedor:
    _nombre:str
    _cuit:str
    _domicilio:str
    _telefono:str
    _proveedores: ClassVar [List["Proveedor"]]=[]  

    def __post_init__(self):        
        self.sort_index=self._nombre
        Proveedor._proveedores.append(self)

    def __str__(self)->str:
        return f'{"Nombre_Proveedor:"}{self._nombre}\n{"CUIT:"}{self._cuit}\n{"Domicilio:"}{self._domicilio}\n{"Telefono:"}{self._telefono}\n'
    
    def __repr__(self):
        return f'{"Nombre_Proveedor:"}{self._nombre}\n{"CUIT:"}{self._cuit}\n{"Domicilio:"}{self._domicilio}\n{"Telefono:"}{self._telefono}\n'
    
    @property 
    def nombre (self):
        return self._nombre
    @nombre.setter
    def set_nombre(self,nombre):
        self._nombre=nombre 

    @property       
    def cuit (self):
        return self._cuit
    @cuit.setter
    def cuit (self,cuit):
        self._cuit=cuit

    @property 
    def domicilio(self):
        return self._domicilio
    @domicilio.setter
    def domicilio (self,domicilio):
        self._domicilio=domicilio

    @property 
    def telefono(self):
        return self._telefono
    @telefono.setter
    def telefono(self,telefono):
        self._telefono=telefono

    
    @classmethod
    def registrar_proveedor(cls):
        op=1
        while(op!=0):    
            nombre_proveedor=input("Ingrese nombre de proveedor: ")
            cuit=input("Ingrese cuit de proveedor: ")
            domicilio=input("Ingrese domicilio de proveedor: ")
            telefono=input("Ingrese número de teléfono: ")
            if ((nombre_proveedor.isspace() or len(nombre_proveedor) ==0) or (cuit.isspace() or len(cuit) ==0) or (domicilio.isspace() or len(domicilio) ==0) or (telefono.isspace() or len(telefono) ==0) ):
                print ("Error, dato/s ingresado/s vacios")
            else:
                cls(nombre_proveedor, cuit, domicilio, telefono)
                print("Proveedor registrado")
            
            op=int(input("Ingrese 1 para continuar con más registros, 0 para salir : "))


    def modificar_atributos():
     
        cuit=input("Ingrese CUIT del proveedor al cual desea modificar sus atributos: ")
        estadoproveedor=0
        for k in Proveedor._proveedores:
            if(k._cuit==cuit):
                print ("Proveedor Encontrado")
                estadoproveedor=1 #Proveedor encontrado    
                print ("------------------------")
                print ("\n Nombre: ", k._nombre) 
                print ("\n CUIT: ",k._cuit)
                print ("\n Domicilio: ", k._domicilio)
                print ("\n Telefono: ", k._telefono)
                print ("\n")
                print ("------------------------")

                nom=input("Ingrese nuevo nombre (presione enter si no desea modificar este atributo): ")            
                if (nom.isspace()or len (nom)==0):
                    print ("No ingreso ningún dato, se conserva nombre actual")
                else:
                    k._nombre=nom
                    print("Se modificó nombre de proveedor")

                domicilio=input("Ingrese nuevo domicilio (presione enter si no desea modificar este atributo): ")
                if (domicilio.isspace() or len(domicilio)==0):
                    print ("No ingreso ningún dato, se conserva domicilio actual")
                else:
                    k._domicilio=domicilio
                    print("Se modificó domicilio de proveedor")
                
                telef=input("Ingrese nuevo número de teléfono (presione enter si no desea modificar este atributo): ")

                if (telef.isspace() or len (telef)==0):
                    print ("No ingresó ningún dato, se conserva número de teléfono actual")
                else:
                    k._telefono=telef        
                    print("Se modificó número de teléfono de proveedor")

        if(estadoproveedor==0):
            print (" El proveedor ingresado no se encuentra registrado")
           
    def mostrar_proveedores():
        print("Lista de Proveedores Registrados: ")
        for k in Proveedor._proveedores:
            print("----------------------------")
            print(k)

    def eliminar_proveedor():
        cuit=input("Ingrese CUIT del proveedor al cual desea eliminar de los registros: ")
        estadoproveedor=0
        for k in Proveedor._proveedores:
            if(k._cuit==cuit):
                print ("Proveedor Encontrado")
                estadoproveedor=1 #Proveedor encontrado    
                print ("------------------------")
                print ("\n Nombre: ", k._nombre) 
                print ("\n CUIT: ",k._cuit)
                print ("\n Domicilio: ", k._domicilio)
                print ("\n Telefono: ", k._telefono)
                print ("\n")
                print ("------------------------")
                Proveedor._proveedores.remove(k)
                print("Proveedor Eliminado")
        if(estadoproveedor==0):
            print("El proveedor ingresado no se encuentra registrado")
        
    