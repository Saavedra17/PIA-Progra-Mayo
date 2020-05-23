#luego de haber hecho el csv se debe importar
import CSV
#primero se crea la clase
class  Contacto:
      def __init__(Nickname,Nombre,Correo,Telefono, FechaNac, Gastos):
            self.Nickname = Nickname
            self.Nombre = Nombre
            self.Correo = Correo
            self.Telefono = Telefono
            self.Gastos = Gastos
with open('Contactos_Mobil.csv') as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter='|')
    contador_lineas = 0
#se debe crear la lista
    lista_Contactos = []

    for linea_datos in lector_csv:
        if contador_lineas == 0:
         print(f'Los nombres de columna son {", ".join(linea_datos)}')
        Else:
         objeto_temporal = Contacto({linea_datos[0]},{linea_datos[1]},{linea_datos[2]},{linea_datos[3]},{linea_datos[4]},{linea_datos[5]})
            lista_incidentes.append(objeto_temporal)
         contador_lineas += 1

    print(f'Procesadas {len(lista_incidentes)} líneas.')
