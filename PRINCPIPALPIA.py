#para trabajar con sistemas operativos
import os
#para trabajar con expresiones regulares
import re
from Clasepia import Contacto

from operator import attrgetter
#se debe comprobar antes de inciciar
def RegEx(_txt,_regex):
    coincidencia=re.match(_regex, _txt)
    return bool(coincidencia)
#Ahora debemos crear el menu
def principal():
    while (True):
        LimpiarPantalla()
        print("Lista de contactos")
        print(" ")
        print("[1] Agregar un contacto.")
        print("[2] Buscar un contacto.")
        print("[3] Eliminar un contacto.")
        print("[4] Mostrar contactos.")
        print("[5] Serializar datos.")
        print("[0] Salir.")
        opcion_elegida = input("¿Qué quieres hacer?  > ")
        if RegEx(opcion_elegida,"^[123450]{1}$"):
            if opcion_elegida=="0":
                print("GRACIAS POR UTILIZAR EL PROGRAMA")
                break
            if opcion_elegida=="1":
                print("Llamar procedimiento para la acción")
            if opcion_elegida=="2":
                print("Llamar procedimiento para la acción")
            if opcion_elegida=="3":
                print("Llamar procedimiento para la acción")
            if opcion_elegida=="4":
                print("Llamar procedimiento para la acción")
            if opcion_elegida=="5":
                print("Llamar procedimiento para la acción")

            input("Presione enter para continuar.")
        else:
            print("Esa respuesta no es válida.")
            input("Presione enter para continuar.")

principal()