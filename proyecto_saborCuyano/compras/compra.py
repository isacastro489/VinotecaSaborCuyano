from dataclasses import dataclass,asdict,astuple, field
from typing import List, ClassVar, Any
from datetime import datetime,time,date
import validaciones.validar as validar
import proveedores.proveedor as prove
import productos.producto as prod


@dataclass (order=True)
class Compras:
    
    _num_factura:str   
    _importe_total:float
    _fecha_compra:date
    _proveedor:str  
    _compras: ClassVar [List["Compras"]]=[]  
    sort_index:Any=field(init=False, repr=False)  
  
    def __post_init__(self):
        Compras._compras.append(self) 
        self.sort_index=self._fecha_compra
      
       

    def __str__(self)->str:
        return f'{"Factura N°:"}{self._num_factura}\n{"Importe Total:"}{self._importe_total}\n{"Fecha de Compra:"}{self._fecha_compra}\n{"Proveedor:"}{self._proveedor}\n'
    
    def __repr__(self):
        return f'{"Factura N°:"}{self._num_factura}\n{"Importe Total:"}{self._importe_total}\n{"Fecha de Compra:"}{self._fecha_compra}\n{"Proveedor:"}{self._proveedor}\n'
    
    @property 
    def numero_factura (self):
        return self._num_factura
    @numero_factura.setter
    def set_numero_factura(self,numero):
        self._num_factura=numero

    @property       
    def importe (self):
        return self._importe_total
    @importe.setter
    def importe (self,importe):
        self._importe_total=importe

    @property 
    def fecha_compra(self):
        return self._fecha_compra
    @fecha_compra.setter
    def fecha_compra (self,fecha):
        self._fecha_compra=fecha
    
    @property 
    def proveedor(self):
        return self._proveedor
    @proveedor.setter
    def proveedor (self,proveedor):
        self._proveedor=proveedor

     
       
    def listar_compras_ordenadas():  

        lista=Compras._compras
        lista= sorted(lista)
        print("-----------------------------------------------")  
        print("Lista Ordenadas de Compras Realizadas por fecha: ") 
        print("-----------------------------------------------") 
        print(lista)     
        return 

    @classmethod
    def registrar_compra(cls):
        
        op=1
        while(op==1): 
              
            numero_factura=input("Ingrese N° de Factura: ")           
            fecha = input("Ingresa fecha de compra en el formato DD/MM/YYYY: ")        
            fecha=datetime.strptime(fecha,'%d/%m/%Y').date()
            try:
                precio=float(input("Ingrese importe total de la compra (int o float): "))
                pre=validar.validarPrecio(precio)
                                                    
            except Exception:
                print("Error en el precio, ingresó string o vacio, ingrese valor valido (int o float)")
                return
            proveedor=input("Ingrese CUIT de proveedor: ")
            estadoproveedor=0 #para saber si se encontró o no al proveedor
            for k in prove.Proveedor._proveedores:
                if(k._cuit==proveedor):
                    print ("Proveedor Encontrado")
                    estadoproveedor=1 #Proveedor encontrado                        
                    print("----------Ingrese detalles de compra--------- ")
                    cod_prod=input("Ingrese código de producto, Ingrese 0 para terminar la carga: ")
                    while(cod_prod!="0"):                        
                        p=0 #para saber si el producto se encontro
                        for m in prod.Producto._productos:                           
                            if(m._codigo==cod_prod):
                                print ("Producto Encontrado")
                                p=1
                                stock=input("Ingrese cantidad de stock comprado: ")
                                try:
                                    st=validar.validarStock(stock)
                                    if(int(st)):                                         
                                        actualizado= m.actualizar_stock_compra(st)
                                        print("Nuevo Stock de ", m._nombre, " es de:", actualizado)
                                        

                                except Exception:
                                        print("Error en el stock, ingrese valor valido (int) que no sea 0")                    

                       
                        if (p==0) :
                            print ("Producto NO ENCONTRADO, ¿Desea registrarlo?")
                            print ("Ingrese 1 si desea registrarlo, ingrese 0 caso contrario")    
                            opcion=int(input("Ingrese una opcion: "))
                            if (opcion==1):
                                prod.Producto.cargar_productos()                                    
                            if(opcion==0):
                                 print("Ud. eligió no registrar producto")
                            if (opcion!=0 and opcion!=1):
                                print("Ud. ingreso opción incorrecta")

                        cod_prod=input("Ingrese siguiente código de producto de su compra, Ingrese 0 para terminar la carga: ")
                    cls(numero_factura,pre,fecha,proveedor)                     
                    print ("Compra Registrada")
                      
            if (estadoproveedor==0):
                print ("Proveedor NO ENCONTRADO, ¿Desea registrarlo?")
                print ("Ingrese 1 si desea registrarlo, ingrese 0 caso contrario")    
                opcion=int(input("Ingrese una opcion: "))
                if (opcion==1):                 
                    prove.Proveedor.registrar_proveedor()                                    
                if(opcion==0):
                    print("Ud. eligió no registrar proveedor")
                if (opcion!=0 and opcion!=1):
                    print("Ud. ingreso opción incorrecta")               

            
            op=int(input("Ingrese 1 para continuar cargando mas compras, 0 para salir : "))
        return

    def informe_gastos_entre_fechas():

        print('\n')
        print ("-----------------------------------------------")
        print ("INFORME: DINERO INVERTIDO EN COMPRAS ENTRE FECHAS")
        print ("-----------------------------------------------")
        print('\n')
        acumulador=0
        fecha_uno= input("Ingresa fecha de compra desde, en el formato DD/MM/YYYY: ")
        fecha_1=datetime.strptime(fecha_uno,'%d/%m/%Y').date()
        fecha_dos= input("Ingresa fecha de compra hasta, en el formato DD/MM/YYYY: ")
        fecha_2=datetime.strptime(fecha_dos,'%d/%m/%Y').date()
        ban=0 # bandera para indicar que existe al menos una compras realizada entre fechas ingresadas
        for c in Compras._compras:                                   
            if((c._fecha_compra >= fecha_1) and (c._fecha_compra <= fecha_2)):
                ban=1
                acumulador=acumulador + c._importe_total
        if(ban==1):
            print ("El Dinero Invertido en Compras entre ", fecha_1, " y ", fecha_2, " es de $ ", acumulador)        
        if(ban==0):
            print("No existen compras realizadas entre fechas ingresadas")


    def compras_entre_fechas():
        print('\n')
        print ("-----------------------------------------------")
        print ("INFORME: DETALLE DE COMPRAS ENTRE FECHAS ")
        print ("-----------------------------------------------")
        print('\n')
        fecha_uno= input("Ingresa fecha de compra desde, en el formato DD/MM/YYYY: ")
        fecha_1=datetime.strptime(fecha_uno,'%d/%m/%Y').date()
        fecha_dos= input("Ingresa fecha de compra hasta, en el formato DD/MM/YYYY: ")
        fecha_2=datetime.strptime(fecha_dos,'%d/%m/%Y').date()
        print ("Las compras realizadas entre fechas son las siguientes: ")
        print('\n')
        ban=0 #para indicar si existe al menos una compra entre fechas ingresadas
        for c in Compras._compras:                                   
            if((c._fecha_compra >= fecha_1) and (c._fecha_compra <= fecha_2)):
                ban=1
                print (c)
                print("-------------------------------")
        if(ban==0):
            print("No existen compras realizadas entre fechas")

    def compras_entre_fechas_proveedor():
        print('\n')
        print ("-----------------------------------------------")
        print ("INFORME: DETALLE DE COMPRAS ENTRE FECHAS REALIZADAS POR UN PROVEEDOR")
        print ("-----------------------------------------------")
        print('\n')
        fecha_uno= input("Ingresa fecha de compra desde, en el formato DD/MM/YYYY: ")
        fecha_1=datetime.strptime(fecha_uno,'%d/%m/%Y').date()
        fecha_dos= input("Ingresa fecha de compra hasta, en el formato DD/MM/YYYY: ")
        fecha_2=datetime.strptime(fecha_dos,'%d/%m/%Y').date()
        proveedor=input("Ingresa CUIT de proveedor: ")
        pro=0 #bandera para indicar si se encontró proveedor
        ban=0 #bandera para indicar que existe al menos una compra a tal proveedor entre fechas ingresadas
        for p in prove.Proveedor._proveedores: 
            if(p._cuit==proveedor):
                nombre=p._nombre 
                pro=1  #proveedor encontrado 
                print("Compras Realizadas por el proveedor: ", nombre, "entre el ", fecha_1, " y ", fecha_2)    
                for c in Compras._compras:    #busca compras realizadas por dicho proveedor                               
                    if((c._fecha_compra >= fecha_1) and (c._fecha_compra <= fecha_2) and(c._proveedor ==proveedor)):
                        ban=1
                        print (c)
                        print("-------------------------------")

                if(ban==0):
                    print("No existe compras realizadas por el proveedor ", proveedor, " entre las fechas ingresadas")
        if(pro==0):
            print ("Proveedor no registrado")