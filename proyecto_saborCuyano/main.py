import menu.menuopciones as menu
import productos.producto as producto
import validaciones.validar as validar
import proveedores.proveedor as proveedor
import vendedores.vendedor as vendedor
import compras.compra as compra
import ventas.venta as venta
from datetime import datetime,time,date

def main():     

    valor=menu.mostrarmenu("MENU DE OPCIONES: VINOTECA SABOR CUYANO ", ["1. OPERAR CON PRODUCTOS","2. OPERAR CON PROVEEDOR", "3. OPERAR CON COMPRAS","4. OPERAR CON VENTAS", "5. OPERAR CON VENDEDORES", "6. SALIR"])
    menus(valor)


def menus(valor:str):
   
    while (valor != "6"): 

        #----------------------
        #OPERAR CON PRODUCTOS> Agregar informes: stock disponible de x producto, etc. agregar proveedor a producto para sacar un informe de cuantos productos nos ofrece x proveedor etc. agregar fecha de vencimiento, ver que proudctos se vencen en x fecha etc.
        #----------------------

        if (valor == "1"): 
            print("---------------SUBMENU PRODUCTOS------------------")
            val=menu.mostrarSubmenu( ["1. REGISTRAR PROODUCTO","2. MODIFICAR PRODUCTO", "3. LISTAR PRODUCTOS REGISTRADOS","4. INFORME PRODUCTOS", "5. SALIR"])           
            while (val!= "5"):
                if(val=='1'):                     
                    producto.Producto.cargar_productos()
                if(val=='2'):
                    producto.Producto.modificar_producto()
                if(val=='3'):
                    producto.Producto.listar_productos_ordenados()
                if(val=='4'): 
                    print("---------------SUBMENU INFORMES PRODUCTOS------------------")                  
                    inf=menu.mostrarSubmenu( ["1. INFORME: STOCK DISPONIBLE DE UN PRODUCTO DETERMINADO","2. INFORME: PRODUCTOS PERTENECIENTES A UN PROVEEDOR DETERMINADO ", "3. INFORME: PRODUCTOS VENCIDOS ENTRE FECHAS", "4. INFORME: PRODUCTOS QUE DEBEN REPONERSE", "5. SALIR"]) 
                    while (inf!='5'):
                        if(inf=='1'):
                            producto.Producto.stock_disponible()                         
                        if(inf=='2'):
                            producto.Producto.productos_proveedor()                           
                        if (inf=='3'):
                            producto.Producto.productos_vencidos()
                        if (inf=='4'):
                            producto.Producto.productos_reponer()
                        if(inf!='1' and inf!='2' and inf!='3' and inf!='4' and inf!='5'):
                            print("Opción ingresada incorrecta")
                        inf=menu.mostrarSubmenu( ["1. INFORME: STOCK DISPONIBLE DE UN PRODUCTO DETERMINADO","2. INFORME: PRODUCTOS PERTENECIENTES A UN PROVEEDOR DETERMINADO ", "3. INFORME: PRODUCTOS VENCIDOS ENTRE FECHAS", "4. INFORME: PRODUCTOS QUE DEBEN REPONERSE", "5. SALIR"]) 
                    #Fin while informes- PRODUCTOS
                    if(inf=='5'):
                        print('Ud. eligió salir de Submenú Informes de Productos')
                if(val!='1' and val!='2' and val!='3' and val!='4' and val!='5'):
                    print("Opción ingresada incorrecta")
                val=menu.mostrarSubmenu( ["1. REGISTRAR PROODUCTO","2. MODIFICAR PRODUCTO", "3. LISTAR PRODUCTOS REGISTRADOS","4. INFORME PRODUCTOS", "5. SALIR"])           
            #Fin while productos
            if (val=='5'):
                print("Ud. eligió salir de Menú Productos...")  

         #----------------------
         #OPERAR CON PROVEEDOR
         #----------------------

        if(valor=="2"):
            print("---------------SUBMENU PROVEEDOR------------------")
            val=menu.mostrarSubmenu( ["1. REGISTRAR PROVEEDOR","2. MODIFICAR PROVEEDOR", "3. MOSTRAR PROVEEDORES","4. ELIMINAR PROVEEDOR","5. SALIR"])           
            while (val!= "5"):
                if(val=='1'):
                    proveedor.Proveedor.registrar_proveedor()
                if(val=='2'):
                    proveedor.Proveedor.modificar_atributos()
                if(val=='3'):
                    proveedor.Proveedor.mostrar_proveedores()
                if(val=='4'):
                    proveedor.Proveedor.eliminar_proveedor()
                if(val!='1' and val!='2' and val!='3' and val!='4' and val!='5'):
                    print("Opción ingresada incorrecta")
                val=menu.mostrarSubmenu( ["1. REGISTRAR PROVEEDOR","2. MODIFICAR PROVEEDOR", "3. MOSTRAR PROVEEDORES","4. ELIMINAR PROVEEDOR","5. SALIR"])           
            #Fin while proveedor
            if (val=='5'):
                print("Ud. eligió salir de  Menú Proveedores...")    
         
         #----------------------
         #OPERAR CON COMPRAS
         #----------------------  

        if (valor=="3"):
            print("---------------SUBMENU COMPRAS------------------")
            val=menu.mostrarSubmenu( ["1. REGISTRAR NUEVA COMPRA","2. LISTAR COMPRAS REALIZADAS", "3. INFORME DE COMPRAS", "4. SALIR"])           
            while (val!= "4"):
                if(val=='1'):
                    compra.Compras.registrar_compra()                   
                if(val=='2'):
                     compra.Compras.listar_compras_ordenadas()
                if(val=='3'):                   
                    inf=menu.mostrarSubmenu( ["1. INFORME: DINERO INVERTIDO EN COMPRAS ENTRE FECHAS","2. INFORME: DETALLE DE COMPRAS REALIZADAS ENTRE FECHAS ", "3. INFORME: COMPRAS ENTRE FECHAS REALIZADAS POR UN PROVEEDOR DETERMINADO", "4. SALIR"]) 
                    while (inf!='4'):
                        if(inf=='1'):
                            compra.Compras.informe_gastos_entre_fechas()                         
                        if(inf=='2'):
                            compra.Compras.compras_entre_fechas()                            
                        if (inf=='3'):
                            compra.Compras.compras_entre_fechas_proveedor()
                        if(inf!='1' and inf!='2' and inf!='3' and inf!='4'):
                            print("Opción ingresada incorrecta")
                        inf=menu.mostrarSubmenu( ["1. INFORME: DINERO INVERTIDO EN COMPRAS ENTRE FECHAS","2. INFORME: DETALLE DE COMPRAS REALIZADAS ENTRE FECHAS ", "3. INFORME: COMPRAS ENTRE FECHAS REALIZADAS POR UN PROVEEDOR DETERMINADO", "4. SALIR"]) 
                    #Fin while informes- compras
                    if (inf=='4'):
                        print("Ud. eligió salir  de Menu Informes...")
                if(val!='1' and val!='2' and val!='3' and val!='4'):
                    print("Opción ingresada incorrecta")                    
                val=menu.mostrarSubmenu( ["1. REGISTRAR NUEVA COMPRA","2. LISTAR COMPRAS REALIZADAS", "3. INFORME DE COMPRAS", "4. SALIR"])                                   
            #Fin while compras
            if (val=='4'):
                print("Ud. eligió salir de Menú de Compras...")

        #----------------------
        #OPERAR CON VENTAS
        #----------------------  

        if (valor=="4"):
            print("---------------SUBMENU VENTAS------------------")
            val=menu.mostrarSubmenu( ["1. REGISTRAR NUEVA VENTA","2. MOSTRAR VENTAS","3. INFORMES DE VENTAS", "4. SALIR"])           
            while (val!= "4"):
                if(val=='1'):
                    venta.Ventas.registrar_venta()
                if(val=='2'):
                    venta.Ventas.listar_ventas_ordenadas()
                if(val=='3'):
                    print("---------------SUBMENU INFORMES DE VENTAS------------------")
                    inf=menu.mostrarSubmenu( ["1. INFORME: VENTAS REGISTRADAS ENTRE FECHAS ","2. INFORME: GANANCIAS OBTENIDAS ENTRE FECHAS ", "3. INFORME: VENTAS REALIZADAS POR UN VENDEDOR DETERMINADO", "4. SALIR"]) 
                    while (inf!='4'):
                        if(inf=='1'):
                            venta.Ventas.ventas_entre_fechas()                     
                        if(inf=='2'):
                            venta.Ventas.ganancias_entre_fechas()                             
                        if (inf=='3'):
                            venta.Ventas.ventas_entre_fechas_proveedor()  
                        if(inf!='1' and inf!='2' and inf!='3' and inf!='4'):
                            print("Opción ingresada incorrecta")
                        inf=menu.mostrarSubmenu( ["1. INFORME: VENTAS REGISTRADAS ENTRE FECHAS ","2. INFORME: GANANCIAS OBTENIDAS ENTRE FECHAS ", "3. INFORME: VENTAS REALIZADAS POR UN VENDEDOR DETERMINADO", "4. SALIR"]) 
                    #Fin while informes- ventas
                    if (inf=='4'):
                        print("Ud. eligió salir  de Menu Informes...")
                if(val!='1' and val!='2' and val!='3' and val!='4'):
                    print("Opción ingresada incorrecta")
                val=menu.mostrarSubmenu( ["1. REGISTRAR NUEVA VENTA","2. MOSTRAR VENTAS","3. INFORMES DE VENTAS", "4. SALIR"])     
            #Fin while ventas
            if(val=='4'):
                print("Ud. eligió salir de Menú Ventas...")
           
        #----------------------
        #OPERAR CON VENDEDORES
        #----------------------

        if (valor=="5"):
            print("---------------SUBMENU VENDEDORES------------------")
            val=menu.mostrarSubmenu( ["1. REGISTRAR VENDEDOR","2. MODIFICAR VENDEDOR", "3. MOSTRAR VENDEDORES","4. ELIMINAR UN VENDEDOR", "5. SALIR"])           
            while (val!= "5"):
                if(val=='1'):
                    vendedor.Vendedor.registrar_vendedor()
                if(val=='2'):
                    vendedor.Vendedor.modificar_atributos()
                if(val=='3'):
                    vendedor.Vendedor.mostrar_vendedores()
                if(val=='4'):
                    vendedor.Vendedor.eliminar_vendedor()
                if(val!='1' and val!='2' and val!='3' and val!='4' and val!='5'):
                    print("Opción ingresada incorrecta")
                val=menu.mostrarSubmenu( ["1. REGISTRAR VENDEDOR","2. MODIFICAR VENDEDOR", "3. MOSTRAR VENDEDORES","4. ELIMINAR UN VENDEDOR", "5. SALIR"])           
            #Fin while vendedor
            if (val=='5'):
                print("Ud. eligió salir de Menú Vendedor...")                 
        
        valor=menu.mostrarmenu("MENU DE OPCIONES: VINOTECA SABOR CUYANO ", ["1. OPERAR CON PRODUCTOS","2. OPERAR CON PROVEEDOR", "3. OPERAR CON COMPRAS","4. OPERAR CON VENTAS", "5. OPERAR CON VENDEDORES", "6. SALIR"])
        
    # fin del while general
    #                     
    if (valor=="6"):               
        print("Ud. eligió salir del Menú General de Vinoteca Sabor Cuyano... Adiós")

    
   
if __name__== "__main__":
    print('\n')
    print ("-----------------------------------------------")
    print ("BIENVENIDOS A MENU DE VINOTECA 'SABOR CUYANO' SAN JUAN")
    print ("-----------------------------------------------")  
  
    try:
        validar.Administrador.validar()
        f3=datetime.strptime("20/06/2023",'%d/%m/%Y').date()
        f4=datetime.strptime("20/06/2023",'%d/%m/%Y').date()
        f5=datetime.strptime("25/06/2023",'%d/%m/%Y').date()
        producto.Producto('1','Malbec',1050, 200, f3, '27-34094891-0')
        producto.Producto('2','Coñac',2050, 200,f4, '27-34094891-0')
        producto.Producto('3','Sirac',1250, 200,f5,'27-34094891-1')  
        proveedor.Proveedor('Bodega Casa Montes','27-34094891-0','Caucete 156 este','2645761655')
        proveedor.Proveedor('Bodega Alto de Sierra','20-34094891-0','Albardon 156 este','2645789456')
        proveedor.Proveedor('Bodega Graffignna','27-34094891-1','Sarmiento 156 este','2645888999')
        f1=datetime.strptime("21/06/2023",'%d/%m/%Y').date()
        f2=datetime.strptime("20/06/2023",'%d/%m/%Y').date()
        compra.Compras('560',25000,f1,'27-34094891-0')
        compra.Compras('750',50000,f2,'20-34094891-0')
        venta.Ventas('020',12000,f1,'34094891')
        venta.Ventas('030',10500,f2,'34094891')
        vendedor.Vendedor('Pedro','Suarez','34094891','Albardon 156 este','2645789456')
        vendedor.Vendedor('Juan','Sanchez','18119051','Rawson 156 este','2645789456')         
        main()                          
    except Exception:
        print ("Contraseña Incorrecta. Usuario no autorizado para realizar esta operación")  
   
    
