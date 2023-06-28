from typing import List
from validaciones.validar import cadenavacia_MENU, cadenavacia_SUBMENU

def mostrarmenu(titulo: str, opciones: List [str]
                )->str:
    try:
        print ()
        print (titulo)
        print ()
        for opcion in opciones:
            print (opcion)

       
        opc= input ("Ingrese la opción: ")     
        opcionvalidada= cadenavacia_MENU (opc)           
        return opcionvalidada

    except Exception:
        print(" A ingresado una opción vacia o inexistente, intente nuevamente")   
        opcionvalidada='-1'
        return opcionvalidada
    
def mostrarSubmenu(opciones: List [str]
                )->str:
    try:
        
        for opcion in opciones:
            print (opcion)

       
        opc= input ("Ingrese la opción: ")     
        opcionvalidada= cadenavacia_SUBMENU (opc)           
        return opcionvalidada

    except Exception:
        print(" A ingresado una opción vacia o inexistente, intente nuevamente")   
        opcionvalidada='-1'
        return opcionvalidada