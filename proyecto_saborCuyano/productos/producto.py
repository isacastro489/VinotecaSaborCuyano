
from dataclasses import dataclass,asdict,astuple, field
from datetime import datetime,time,date
from typing import List, ClassVar, Any
import validaciones.validar as validar
import proveedores.proveedor as prove



@dataclass (order=True)
class Producto:
    
    _codigo:str
    _nombre:int
    _precio:float
    _stock:int
    _fecha_vencimiento:date 
    _proveedor:str
    _productos: ClassVar [List["Producto"]]=[]     
    _stockminimo: ClassVar[int] = 20  
    sort_index:Any=field(init=False, repr=False)  
  
    def __post_init__(self):

        
        self.sort_index=self._nombre
        Producto._productos.append(self)

    def __str__(self)->str:
        return f'{"Codigo:"}{self._codigo}\n{"Nombre:"}{self._nombre}\n{"Precio:"}{self._precio}\n{"Stock:"}{self._stock}\n{"Stock_Minimo:"}{self._stockminimo}\n{"Fecha de Vencimiento:"}{self._fecha_vencimiento}\n{" Proveedor :"}{self._proveedor}\n'
    
    def __repr__(self):
        return f'{"Codigo:"}{self._codigo}\n{"Nombre:"}{self._nombre}\n{"Precio:"}{self._precio}\n{"Stock:"}{self._stock}\n{"Stock_Minimo:"}{self._stockminimo}\n{"Fecha de Vencimiento:"}{self._fecha_vencimiento}\n{" Proveedor :"}{self._proveedor}\n'
    
    @property 
    def precio (self)->float:
        return self._precio
    @precio.setter
    def precio (self,precio:float)->None:
        self._precio=precio  

    @property       
    def codigo(self):
        return self._codigo
    @codigo.setter
    def codigo(self,codigo):
        self._codigo=codigo

    @property 
    def nombreproducto(self):
        return self._nombre
    @nombreproducto.setter
    def nombreproducto(self,prod):
        self._nombre=prod

    @property     
    def stock(self):
        return self._stock
    @stock.setter
    def stock(self, stock):
        self._stock=stock
    @property     
    def stockminimo(self):
        return self._stockminimo
    @stockminimo.setter
    def stockminimo(self, stock):
        self._stockminimo=stock
    
    @property     
    def fecha_vencimiento(self):
        return self._fecha_vencimiento
    @fecha_vencimiento.setter
    def fecha_vencimiento(self, fecha):
        self._fecha_vencimiento=fecha

    @property     
    def proveedor(self):
        return self._proveedor
    @proveedor.setter
    def proveedor(self, proveedor):
        self._proveedor=proveedor

    def actualizar_stock_compra(self, cantidad:int)->int:
        self._stock=self._stock + cantidad
        
        return self._stock 

    
    def actualizar_stock_venta(self, cantidad:int)->int:
        self._stock=self._stock - cantidad
        
        return self._stock 
    

   
    def listar_productos_ordenados(): 
       
        print ("------------------------------")
        print ("PRODUCTOS ORDENADOS POR NOMBRE")
        print ("------------------------------")
      
        lista=Producto._productos
        lista=Producto._productos
        lista= sorted(lista)  
        print(lista)
        return    

    @classmethod
    def cargar_productos(cls):
        op=1
        pr=0 #para indicar si se encontró proveedor buscado
        while(op!=0):    
            codigo=input("Ingrese codigo del producto: ")
            nombreprod=input("Ingrese nombre del producto: ")
            try:
                precio=float(input("Ingrese precio del producto (int o float) que no sea valor 0: "))
                pre=validar.validarPrecio(precio)
                                                    
            except Exception:
                print("Error en el precio, ingresó string o vacio, ingrese valor valido (int o float) que no sea valor 0")
                return
            fecha = input("Ingresa fecha de vencimiento del producto, en el formato DD/MM/YYYY: ")            
            fecha=datetime.strptime(fecha,'%d/%m/%Y').date()  
            proveedor=input("Ingrese CUIT del Proveedor del Producto: ") 
            for p in prove.Proveedor._proveedores:
                if(p._cuit==proveedor):
                    pr=1
                    print("Proveedor Encontrado: ")
                    stock=input("Ingrese stock (si no desea ingresar el mismo, presione enter, el mismo se inicializará en 0) : ")
                    if (stock.isspace() or len(stock) ==0):
                        print ("No ingreso nada,stock se inicializa en 0")
                        stock=0
                    else:
                        try:
                            pre=validar.validarCadena(stock)
                            if(int(pre)): 
                                stock=pre                  

                        except Exception:
                            print("Error en el stock, ingrese valor valido (int)")                    
                            return           
            
                    cls(codigo, nombreprod, precio,stock, fecha,proveedor)
                    print("Producto Registrado ")
            if(pr==0):
                print ("Proveedor No Registrado")
                print ("Ingrese 1 si desea registrar proveedor, ingrese 0 caso contrario")    
                opcion=int(input("Ingrese una opcion: "))
                if (opcion==1):                 
                    prove.Proveedor.registrar_proveedor()                                    
                if(opcion==0):
                    print("Ud. eligió no registrar proveedor")
                if (opcion!=0 and opcion!=1):
                    print("Ud. ingreso opción incorrecta")    
            op=int(input("Ingrese 1 para continuar con más registros de productos, 0 para salir : "))
        return
    
    @classmethod
    def modificar_producto(cls):
        i=False
        codigo= input ("Ingrese código de producto a modificar: ")
        
        for k in Producto._productos:
            if(k._codigo==codigo):
                print("Producto Encontrado: ")
                print(k)
                i=True
                nom=input("Ingrese nuevo nombre de producto (presione Enter, si no desea modificar este atributo):  ")           
                if (nom.isspace()or len (nom)==0):
                    print ("No ingreso ningún dato, se conserva nombre actual")
                else:
                    k._nombre=nom
                    print("Se modificó nombre de producto")
                
                
                precio=input("Ingrese nuevo precio del producto (presione Enter, si no desea modificar este atributo):  ")
                if (precio.isspace() or len(precio) ==0):
                    print ("No ingreso ningún dato, se conserva precio actual")
          
                else:
                    try:
                        pre=validar.validarCadena(precio)
                        if(float(pre)): 
                            k._precio=pre
                            print ("Se modificó nombre de producto")                  

                    except Exception:
                        print("Error en el precio, ingrese valor valido (float o int)")                    
                        return          
                
                stockminimo=input("Ingrese nuevo stock minimo (presione Enter, si no desea modificar este atributo): ")

                if (stockminimo.isspace() or len (stockminimo)==0):
                    print ("No ingresó ningún dato, se conserva stock minimo actual")
                else:
                    try:
                        st=validar.validarCadena(stockminimo)
                        if(float(st)): 
                            k._stockminimo=st
                            print ("Se modificó stock minimo del producto")                  

                    except Exception:
                        print("Error en el stock minimo, ingrese valor valido (float o int)")                    
                        return    
                    
               
                print ("ATRIBUTOS ACTUALIZADOS : ")   
                print (k)                

        if(i==False):
                print ("El producto que intenta modificar atributos no se encuentra registrado en nuestra Base de Datos")
       
    def stock_disponible():
        print('\n')
        print ("----------------------------------------------------")
        print ("INFORME: STOCK DISPONIBLE DE UN PRODUCTO DETERMINADO")
        print ("-----------------------------------------------------")
        print('\n')
        codigo=input("Ingrese codigo del producto: ")
        for p in Producto._productos:
            if(p._codigo==codigo):
                print("Producto Encontrado: ", p._nombre)
                print ("El stock disponible de este producto es: ", p._stock, " unidades" )
                return
    
    def productos_proveedor():
        pr=0 #para saber si se encontró proveedor buscado
        ban=0
        print('\n')
        print ("------------------------------------------------------------")
        print ("INFORME: PRODUCTOS PERTENECIENTES A UN PROVEEDOR DETERMINADO")
        print ("------------------------------------------------------------")
        print('\n')
        proveedor=input ("\n Ingrese CUIT de proveedor: ")
        for p in prove.Proveedor._proveedores:
                if(p._cuit==proveedor):
                    pr=1
                    print("Proveedor Encontrado: ")
                    print ("Los productos registrados para este proveedor son: ")
                    for p in Producto._productos:
                        if(p._proveedor==proveedor):
                            ban=1
                            print('\n')
                            print(p)                        
        if(pr==0):
            print("Proveedor No Registrado")
        if(ban==0):
            print("El proveedor ingresado no tiene productos registrados en nuestra base de datos ")
    
    def productos_vencidos():
        print('\n')
        print ("----------------------------------------")
        print ("INFORME: PRODUCTOS VENCIDOS ENTRE FECHAS")
        print ("-----------------------------------------")
        print('\n')
        ban=0
        fecha_uno= input("Ingresa fecha de vencimiento desde, en el formato DD/MM/YYYY: ")
        fecha_1=datetime.strptime(fecha_uno,'%d/%m/%Y').date()
        fecha_dos= input("Ingresa fecha de vencimiento hasta, en el formato DD/MM/YYYY: ")
        fecha_2=datetime.strptime(fecha_dos,'%d/%m/%Y').date()
        print ("\n Los productos a vencidos entre dicha fecha son: ")
        for p in Producto._productos:                                   
            if ((p._fecha_vencimiento >= fecha_1) and (p._fecha_vencimiento <= fecha_2) ):
                ban=1
                print (p)
                print('\n')
      
        if(ban==0):
            print("No existen productos vencidos entre fechas ingresadas")

    def productos_reponer():
        print('\n')
        print ("----------------------------------------")
        print ("INFORME: PRODUCTOS QUE DEBEN REPONERSE")
        print ("-----------------------------------------")
        print('\n')
        ban=0
        print (" Los productos que deben reponerse, porque llegaron a su stock minimo son: ")
        print('\n')
        for p in Producto._productos:                                   
            if (p._stock <= p._stockminimo ):                
                print (p)
                ban=1
                print('\n')
        if (ban==0):
            print (" No existen productos que deban reponerse, su stock está por encima del stock minimo")