from dataclasses import dataclass,asdict,astuple, field
from typing import List, ClassVar, Any
from datetime import datetime,time,date
import validaciones.validar as validar

@dataclass (order=True)
class Vendedor:
    _nombre:str
    _apellido:str
    _dni:str
    _domicilio:str
    _telefono:str
    _vendedores: ClassVar [List["Vendedor"]]=[]  

    def __post_init__(self):        
        self.sort_index=self._apellido
        Vendedor._vendedores.append(self)

    def __str__(self)->str:
        return f'{"Nombre_Vendedor:"}{self._nombre}\n{"Apellido_Vendedor:"}{self._apellido}\n{"DNI:"}{self._dni}\n{"Domicilio:"}{self._domicilio}\n{"Telefono:"}{self._telefono}\n'
    
    def __repr__(self):
        return f'{"Nombre_Vendedor:"}{self._nombre}\n{"Apellido_Vendedor:"}{self._apellido}\n{"DNI:"}{self._dni}\n{"Domicilio:"}{self._domicilio}\n{"Telefono:"}{self._telefono}\n'
    
    @property 
    def nombre (self):
        return self._nombre
    @nombre.setter
    def set_nombre(self,nombre):
        self._nombre=nombre 

    @property 
    def apellido (self):
        return self._apellido
    @apellido.setter
    def set_apellido(self,apellido):
        self._apellido=apellido


    @property       
    def dni (self):
        return self._dni
    @dni.setter
    def dni (self,dni):
        self._dni=dni

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
    def registrar_vendedor(cls):
        op=1
        while(op!=0):            
            try:
                dni=input("Ingrese DNI del vendedor (sin puntos,guiones, ni espacios): ")
                validar.validar_dni(dni)
            except Exception:
                print(f'DNI ingresado: {dni} no es valido')
             
            try:    
                nombre_vendedor=input("Ingrese nombre del vendedor: ")
                apellido_vendedor=input("Ingrese apellido del vendedor: ")
                domicilio=input("Ingrese domicilio de proveedor: ")
                telefono=input("Ingrese número de teléfono: ")
                validar.validar_cadena_string(nombre_vendedor, apellido_vendedor, domicilio, telefono)
                cls(nombre_vendedor, apellido_vendedor,dni, domicilio, telefono)
                print("Vendedor registrado")
            except Exception:
                print(" Error: A ingresado datos vacios")      
 
            op=int(input("Ingrese 1 para continuar con más registros, 0 para salir : "))


    def modificar_atributos():
     
        dni=input("Ingrese DNI del vendedor al cual desea modificar sus atributos: ")
        estadovendedor=0
        for k in Vendedor._vendedores:
            if(k._dni==dni):
                print ("Vendedor Encontrado")
                estadovendedor=1 #vendedor encontrado    
                print ("------------------------")
                print ("\n Nombre: ", k._nombre)
                print ("\n Apellido: ", k._apellido)  
                print ("\n DNI: ",k._dni)
                print ("\n Domicilio: ", k._domicilio)
                print ("\n Telefono: ", k._telefono)
                print ("\n")
                print ("------------------------")

                nom=input("Ingrese nuevo nombre (presione enter si no desea modificar este atributo): ")            
                if (nom.isspace()or len (nom)==0):
                    print ("No ingreso ningún dato, se conserva nombre actual")
                else:
                    k._nombre=nom
                    print("Se modificó nombre de vendedor")
                
                ap=input("Ingrese nuevo apellido (presione enter si no desea modificar este atributo): ")            
                if (ap.isspace()or len (ap)==0):
                    print ("No ingreso ningún dato, se conserva apellido actual")
                else:
                    k._apellido=ap
                    print("Se modificó apellido de proveedor")

                domicilio=input("Ingrese nuevo domicilio (presione enter si no desea modificar este atributo): ")
                if (domicilio.isspace() or len(domicilio)==0):
                    print ("No ingreso ningún dato, se conserva domicilio actual")
                else:
                    k._domicilio=domicilio
                    print("Se modificó domicilio del vendedor")
                
                telef=input("Ingrese nuevo número de teléfono (presione enter si no desea modificar este atributo): ")

                if (telef.isspace() or len (telef)==0):
                    print ("No ingresó ningún dato, se conserva número de teléfono actual")
                else:
                    k._telefono=telef        
                    print("Se modificó número de teléfono del vendedor")

        if(estadovendedor==0):
            print (" El vendedor ingresado no se encuentra registrado")
           
    def mostrar_vendedores():
        print("Lista de Vendedores Registrados: ")
        for k in Vendedor._vendedores:
            print("----------------------------")
            print(k)

    def eliminar_vendedor():
        dni=input("Ingrese DNI del vendedor al cual desea eliminar de los registros: ")
        estadovendedor=0
        for k in Vendedor._vendedores:
            if(k._dni==dni):
                print ("Vendedor Encontrado")
                estadovendedor=1 #Vendedor encontrado    
                print ("------------------------")
                print ("\n Nombre: ", k._nombre) 
                print ("\n Apellido: ", k._apellido) 
                print ("\n DNI: ",k._dni)
                print ("\n Domicilio: ", k._domicilio)
                print ("\n Telefono: ", k._telefono)
                print ("\n")
                print ("------------------------")
                Vendedor._vendedores.remove(k)
                print("Vendedor Eliminado")
        if(estadovendedor==0):
            print("El vendedor ingresado no se encuentra registrado")
        
    