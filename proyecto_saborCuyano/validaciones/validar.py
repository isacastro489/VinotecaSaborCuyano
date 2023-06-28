from typing import List

class Administrador:
  
    usu="Administrador"
    contra="Hola"

    def get_contrasena ()->str:
        return Administrador.contra
    def validar()->bool:    
        contra= input ("Ingrese contraseña: ")      
        if (contra==Administrador.get_contrasena()):                                
            return True
        else:
            raise Exception()  

def cadenavacia_MENU (entrada)->str:
    """recibe un cadena y valida si no esta vacia, devuelve valor"""
    if  (len(entrada)> 0 and ((entrada == "1") | (entrada =="2")| (entrada == "3")| (entrada == "4")| (entrada == "5")| (entrada == "6"))):
        if (entrada == "1"):
            
            return "1"
        if (entrada == "2"):
          
            return "2"
        if (entrada == "3"):
            
            return "3"  
        if (entrada == "4"):
           
            return "4"   
        if (entrada == "5"):
       
            return "5" 
        if (entrada == "6"):
           
            return "6"    

    else:
        raise Exception ()
def cadenavacia_SUBMENU (entrada)->str:
    """recibe un cadena y valida si no esta vacia, devuelve valor"""
    if  (len(entrada)> 0 and ((entrada == "1") | (entrada =="2")| (entrada == "3")| (entrada == "4")| (entrada == "5"))):
        if (entrada == "1"):
            
            return "1"
        if (entrada == "2"):
            
            return "2"
        if (entrada == "3"):
           
            return "3"  
        if (entrada == "4"):           
            return "4"  
        if (entrada == "5"):           
            return "5"    

    else:
        raise Exception ()
      

def validarPrecio(entrada)->float:

        if (entrada!=""):
            if (float(entrada)):
                if(entrada!=0): #que no sea un precio valor 0
                    return entrada
                else: 
                    raise Exception()
            else:
                raise Exception()
        else:
            raise Exception ()
        
def validarCadena(entrada)->str:

        st=float(entrada) 

        if(float(st)):
            return st
        else: 
            raise Exception ()
        
def validarStock(entrada)->int:
             
       st=int(entrada)
       if(int(st)):
            return st
       else: 
            raise Exception ()
       
def validar_dni(entrada)->bool:
      dni=int(entrada) 
      if(int(dni)):
            if (len(entrada) >= 7 and len(entrada) <= 8):                
                return True
            else:
                 raise Exception()
      else:
        raise Exception ()
def validar_cadena_string(nombre, apellido,domicilio, telefono):
    if ((nombre.isspace() or len(nombre) ==0) or (apellido.isspace() or len(apellido) ==0) or (domicilio.isspace() or len(domicilio) ==0) or (telefono.isspace() or len(telefono) ==0) ):
        raise Exception
    else:
        return True