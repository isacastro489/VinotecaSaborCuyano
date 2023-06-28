from dataclasses import dataclass,asdict,astuple, field
from typing import List, ClassVar, Any
from datetime import datetime,time,date
import validaciones.validar as validar
import vendedores.vendedor as vendedor
import productos.producto as prod

@dataclass (order=True)
class Ventas:
    
    _num_factura:str   
    _importe_total:float
    _fecha_venta:date
    _vendedor:str  
    _ventas: ClassVar [List["Ventas"]]=[]  
    sort_index:Any=field(init=False, repr=False)  
  
    def __post_init__(self):
        Ventas._ventas.append(self) 
        self.sort_index=self._fecha_venta     
       
    def __str__(self)->str:
        return f'{"Factura N°:"}{self._num_factura}\n{"Importe Total:"}{self._importe_total}\n{"Fecha de Venta:"}{self._fecha_venta}\n{"Vendedor:"}{self._vendedor}\n'
    
    def __repr__(self):
        return f'{"Factura N°:"}{self._num_factura}\n{"Importe Total:"}{self._importe_total}\n{"Fecha de Venta:"}{self._fecha_venta}\n{"Vendedor:"}{self._vendedor}\n'
    
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
    def fecha_venta(self):
        return self._fecha_venta
    @fecha_venta.setter
    def fecha_venta (self,fecha):
        self._fecha_venta=fecha
    
    @property 
    def vendedor(self):
        return self._vendedor
    @vendedor.setter
    def vendedor (self,vendedor):
        self._vendedor=vendedor
     
    def listar_ventas_ordenadas():  

        lista=Ventas._ventas
        lista= sorted(lista)
        print("-----------------------------------------------")  
        print("Lista Ordenadas de Ventas Realizadas por fecha: ") 
        print("-----------------------------------------------") 
        print(lista)     
        return 

    @classmethod
    def registrar_venta(cls):
        
        op=1
        while(op==1): 
              
            numero_factura=input("Ingrese N° de Factura: ")           
            fecha = input("Ingresa fecha de venta en el formato DD/MM/YYYY: ")
            datetime.strptime(fecha,'%d/%m/%Y')
            fecha=datetime.strptime(fecha,'%d/%m/%Y').date()
            try:
                precio=float(input("Ingrese importe total de la venta (int o float): "))
                pre=validar.validarPrecio(precio)
                                                    
            except Exception:
                print("Error en el importe, ingresó string o vacio, ingrese valor valido (int o float)")
                return
            try:
                dni=input("Ingrese DNI del vendedor (sin puntos,guiones, ni espacios): ")
                validar.validar_dni(dni)
                for k in vendedor.Vendedor._vendedores:
                    if(k._dni==dni):
                        print ("Vendedor Encontrado")
                        estadovendedor=1 #vendedor encontrado                        
                        print("----------Ingrese detalles de venta--------- ")
                        cod_prod=input("Ingrese código de producto, Ingrese 0 para terminar la carga: ")
                        while(cod_prod!="0"):                        
                            p=0 #para saber si el producto se encontro
                            for m in prod.Producto._productos:                           
                                if(m._codigo==cod_prod):
                                    print ("Producto Encontrado")
                                    p=1
                                    
                                    try:
                                        stock=int(input("Ingrese cantidad de stock vendido: "))
                                        st=validar.validarStock(stock)
                                        print("Hola",st)
                                     
                                        if(m._stock >= st):
                                                print ("Stock Disponible")                               
                                                actualizado= m.actualizar_stock_venta(st)
                                                print ("La venta se ha realizado correctamente")
                                                print("Nuevo Stock de ", m._nombre, " es de:", actualizado)                                        
                                        else:
                                                print("Stock insuficiente para realizar la venta:")
                                                print("Stock disponible de este producto es de :", m._stock)                                            

                                    except Exception:
                                            print("Error en el stock, ingrese valor valido (int)")                    
                        
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

                            cod_prod=input("Ingrese siguiente código de producto de su venta, Ingrese 0 para terminar la carga: ")
                        cls(numero_factura,pre,fecha,dni)                     
                        print ("Venta Registrada")
                        
                if (estadovendedor==0):#para saber si se encontró o no al vendedor
                    print ("Vendedor NO ENCONTRADO, ¿Desea registrarlo?")
                    print ("Ingrese 1 si desea registrarlo, ingrese 0 caso contrario")    
                    opcion=int(input("Ingrese una opcion: "))
                    if (opcion==1):                 
                        vendedor.Vendedor.registrar_vendedor()                                    
                    if(opcion==0):
                        print("Ud. eligió no registrar vendedor")
                    if (opcion!=0 and opcion!=1):
                        print("Ud. ingreso opción incorrecta")             
                
                op=int(input("Ingrese 1 para continuar cargando mas ventas, 0 para salir: "))          

            except Exception:
                print(f'DNI ingresado: {dni} no es valido')
                return

    def ventas_entre_fechas():
        print('\n')
        print ("----------------------------------------------------")
        print ("INFORME: DETALLE DE VENTAS REGISTRADAS ENTRE FECHAS ")
        print ("----------------------------------------------------")
        print('\n')
        fecha_uno= input("Ingresa fecha de venta desde, en el formato DD/MM/YYYY: ")
        fecha_1=datetime.strptime(fecha_uno,'%d/%m/%Y').date()
        fecha_dos= input("Ingresa fecha de venta hasta, en el formato DD/MM/YYYY: ")
        fecha_2=datetime.strptime(fecha_dos,'%d/%m/%Y').date()
        print ("Las ventas registradas entre fechas son las siguientes: ")
        print('\n')
        ban=0 #para indicar si existe al menos una venta entre fechas ingresadas
        for v in Ventas._ventas:                                   
            if((v._fecha_venta >= fecha_1) and (v._fecha_venta <= fecha_2)):
                ban=1
                print (v)
                print("-------------------------------")
        if(ban==0):
            print("No existen ventas realizadas entre fechas")


    def ganancias_entre_fechas():        
        print('\n')
        print ("-----------------------------------------------")
        print ("INFORME: GANANCIAS OBTENIDAS ENTRE FECHAS ")
        print ("-----------------------------------------------")
        print('\n')
        acumulador=0
        fecha_uno= input("Ingresa fecha de venta desde, en el formato DD/MM/YYYY: ")
        fecha_1=datetime.strptime(fecha_uno,'%d/%m/%Y').date()
        fecha_dos= input("Ingresa fecha de venta hasta, en el formato DD/MM/YYYY: ")
        fecha_2=datetime.strptime(fecha_dos,'%d/%m/%Y').date()
        print ("Las ventas registradas entre fechas son las siguientes: ")
        print('\n')
        ban=0 #para indicar si existe al menos una venta entre fechas ingresadas
        for v in Ventas._ventas:                                   
            if((v._fecha_venta >= fecha_1) and (v._fecha_venta <= fecha_2)):
                ban=1
                acumulador=acumulador + v._importe_total
             
        if(ban==1):
            print("Las ganancias obtenidas entre fechas es de: ", acumulador , "pesos")
        if(ban==0):
            print("No existen ventas realizadas entre fechas")

    def ventas_entre_fechas_proveedor():
        print('\n')
        print ("-----------------------------------------------")
        print ("INFORME: VENTAS REALIZADAS POR UN VENDEDOR DETERMINADO")
        print ("-----------------------------------------------")
        print('\n')
        fecha_uno= input("Ingresa fecha de venta desde, en el formato DD/MM/YYYY: ")
        fecha_1=datetime.strptime(fecha_uno,'%d/%m/%Y').date()
        fecha_dos= input("Ingresa fecha de venta hasta, en el formato DD/MM/YYYY: ")
        fecha_2=datetime.strptime(fecha_dos,'%d/%m/%Y').date()
        try:
            dni=input("Ingrese DNI del vendedor (sin puntos,guiones, ni espacios): ")
            validar.validar_dni(dni)
            vend=0 #bandera para indicar si se encontró vendedor
            ban=0 #bandera para indicar que existe al menos una venta realizada por el vendedor indicado, entre fechas ingresadas
            for v in vendedor.Vendedor._vendedores: 
                if(v._dni==dni):
                    nombre=v._nombre 
                    vend=1  #vendedor encontrado 
                    print("Ventas Realizadas por el vendedor: ", nombre, "entre el ", fecha_1, " y ", fecha_2)    
                    for v in Ventas._ventas:    #busca ventas realizadas por dicho vendedor                             
                        if((v._fecha_venta >= fecha_1) and (v._fecha_venta <= fecha_2) and(v._vendedor==dni)):
                            ban=1
                            print (v)
                            print("-------------------------------")

                    if(ban==0):
                        print("No existen ventas realizadas por el vendedor ", nombre, " entre las fechas ingresadas")
            if(vend==0):
                print ("vendedor no registrado")

        except Exception:
                print(f'DNI ingresado: {dni} no es valido')